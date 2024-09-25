import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# Input: pd.DataFrame
# Output: dictionary[agent] = [roles of `str` type] of length 3
def make_role_dict(df):
    n = len(df)
    d = {}
    for i in range(0, n):
        name, ar, tr1, tr2, tr3 = df.iloc[i]
        x = [tr1, tr2, tr3]
        y = []
        d[name] = y
        for tr in x:
            if type(tr) != float and type(tr) != np.float64:
                y.append(tr)
    return d

# Input: pd.DataFrame
# Output: dictionary[country] = [language of `str` type] of length 2
def make_language_dict(df):
    n = len(df)
    d = {}
    for i in range(0, n):
        name, lang1, lang2, lang3 = df.iloc[i]
        x = [lang1, lang2, lang3]
        y = []
        d[name] = y
        for lang in x:
            if type(lang) != float and type(lang) != np.float64:
                y.append(lang)
    return d

# Input: pd.DataFrame
# Output: dictionary[country] = shorthand of `str` type
def make_shorthand_dict(df):
    n = len(df)
    d = {}
    for i in range(0, n):
        name, sh = df.iloc[i]
        d[name] = sh
    return d

# Input: pd.DataFrame
# Output: dictionary[country] = shorthand of `int` type
def make_standings_dict(df):
    n = len(df)
    d = {}
    for i in range(0, n):
        name, standing = df.iloc[i]
        d[name] = standing
    return d

# Input: string(country), dictionary(country_dict), string(default_language)
# Output: [language of `str` type] of length 3
def map_languages(country, country_dict, current_languages):
    if country not in country_dict:
        return ['Country not mapped','Country not mapped', 'Country not mapped']
    languages = current_languages.copy()
    mapped_languages = country_dict[country]
    for mapped_lang in mapped_languages:
        if len(languages) >= 3:
            break
        if mapped_lang not in languages:
            languages.append(mapped_lang)
    while len(languages) < 3:
        languages.append('NaN')
    return languages

# Input: list of `str` type, dictionary(agent_dct)
# Output: role of `str` type
def map_role(agents, agent_dct):
    count = {}
    for agent in agents:
        roles = agent_dct[agent]
        for role in roles:
            if role not in count:
                count[role] = 0
            count[role] += 1
    curr = 0
    y = 'Not Found'
    for role, freq in count.items():
        if freq > curr:
            curr = freq
            y = role
    return y
    
# Input: full_name of `str` type, dictionary(shorthand_dict of `str` type)
# Output: shorthand of `str` type
def map_shorthand(full_name, sh_dict):
    if full_name not in sh_dict:
        return 'Team not Mapped'
    return sh_dict[full_name]

# Input: full_name of `str` type, dictionary(standings_dict of `int` type or `str` type if unmapped)
# Output: shorthand of `int` type
def map_standing(full_name, standings_dict):
    if full_name not in standings_dict:
        return 'Team not Mapped'
    return standings_dict[full_name]


# Input: url of `str` type, 
#   col of `list` type, 
#   agent_dict of `dict` type, 
#   country_dict of `dict` type, 
#   sh_dict of `dict` type, 
#   main_lang of `str` type
# Output: pd.DataFrame
def get_table(url, main_lang, role_dict, language_dict, shorthand_dict, standings_dict):
    col = ['country', 'ign', 'language_1', 'language_2', 'language_3', 'team_name_full', 'shorthand', 'standings',
            'agent_1','agent_2','agent_3', 'role', 'maps',
            'k','d','a','kd','kda','acs_per_map','k_per_map','d_per_map','a_per_map']
    new_col = ['country', 'ign', 'team_name_full', 'shorthand', 'standings',
            'role', 'agent_1','agent_2','agent_3', 'maps',
            'k','d','a','kd','kda','acs_per_map', 'k_per_map', 'd_per_map', 'a_per_map',
            'language_1', 'language_2', 'language_3']
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('tbody').find_all('tr')

    data = []
    for i in table:
        data_row = []
        row = i.find_all('td')
        n = len(row)
        flag = True
        for j in range(0, n):
            if j == 0:
                continue
            elif j == 1: # `country`, `ign`, `language_1/2/3`
                country = row[j].find('img')['alt']
                player = row[j].text.strip()
                if country == '':
                    country = 'International'
                languages = map_languages(country, language_dict, main_lang)
                data_row.append(country)
                data_row.append(player)
                for lang in languages:
                    data_row.append(lang)
            elif j == 2: # `team_full_name`, `shorthand`, `standings`
                tag = row[j].find("span")
                if tag is None:
                    flag = False
                    break
                team = tag.get('data-highlightingclass', 'Team Not Mapped')
                if team == 'Team Not Mapped':
                    flag = False
                    break
                shorthand = map_shorthand(team, shorthand_dict)
                standings = map_standing(team, standings_dict)
                data_row.append(team)
                data_row.append(shorthand)
                data_row.append(standings)
            elif j == 3: # `agent_1/2/3` , `role`
                tags = row[j].find_all('a')
                agents = []
                for i in range(0, 3):
                    if i+1 > len(tags):
                        data_row.append('NaN')
                    else:
                        data_row.append(tags[i]['title'])
                        agents.append(tags[i]['title'])
                data_row.append(map_role(agents, role_dict))
            else:
                data_row.append(row[j].text.strip())
        if flag:
            data.append(data_row)
    df = pd.DataFrame(data[1:], columns = col)
    df = df[new_col]
    return df

# Another table present in url that needs to be ignored
# Input: url of `str` type, 
#   col of `list` type, 
#   agent_dict of `dict` type, 
#   country_dict of `dict` type, 
#   sh_dict of `dict` type, 
#   main_lang of `str` type
# Output: pd.DataFrame
def get_table_ignore_table(url, main_lang, role_dict, language_dict, shorthand_dict, standings_dict):
    col = ['country', 'ign', 'language_1', 'language_2', 'language_3', 'team_name_full', 'shorthand', 'standings',
            'agent_1','agent_2','agent_3', 'role', 'maps',
            'k','d','a','kd','kda','acs_per_map','k_per_map','d_per_map','a_per_map']
    new_col = ['country', 'ign', 'team_name_full', 'shorthand', 'standings',
            'role', 'agent_1','agent_2','agent_3', 'maps',
            'k','d','a','kd','kda','acs_per_map', 'k_per_map', 'd_per_map', 'a_per_map',
            'language_1', 'language_2', 'language_3']
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all('tbody')[2].find_all('tr')

    data = []
    for i in table:
        data_row = []
        row = i.find_all('td')
        n = len(row)
        for j in range(0, n):
            if j == 0:
                continue
            elif j == 1: # `country`, `ign`, `language_1/2/3`
                country = row[j].find('img')['alt']
                player = row[j].text.strip()
                if country == '':
                    country = 'International'
                languages = map_languages(country, language_dict, main_lang)
                data_row.append(country)
                data_row.append(player)
                for lang in languages:
                    data_row.append(lang)
            elif j == 2: # `team_full_name`, `shorthand`, `standings`
                team = row[j].find("span")['data-highlightingclass']
                shorthand = map_shorthand(team, shorthand_dict)
                standings = map_standing(team, standings_dict)
                data_row.append(team)
                data_row.append(shorthand)
                data_row.append(standings)
            elif j == 3: # `agent_1/2/3` , `role`
                tags = row[j].find_all('a')
                agents = []
                for i in range(0, 3):
                    if i+1 > len(tags):
                        data_row.append('NaN')
                    else:
                        data_row.append(tags[i]['title'])
                        agents.append(tags[i]['title'])
                data_row.append(map_role(agents, role_dict))
            else:
                data_row.append(row[j].text.strip())
        data.append(data_row)
    df = pd.DataFrame(data[1:], columns = col)
    df = df[new_col]
    return df

