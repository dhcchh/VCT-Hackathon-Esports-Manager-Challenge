import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import glob
import os

def make_role_dict(df):
    """
    Create a dictionary mapping agent names to their roles.

    Parameters:
        df (pd.DataFrame): A DataFrame containing agent names in the first column
            and their corresponding roles in subsequent columns.

    Return type:
        dict: A dictionary where the keys are agent names (str) and the 
            values are lists of roles (str) of length 3.
    """
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

def make_language_dict(df):
    """
    Create a dictionary mapping country names to lists of languages.

    Parameters:
        df (pd.DataFrame): A DataFrame containing country names in the first column
            and their corresponding languages in subsequent columns.

    Return type:
        dict: A dictionary where the keys are country names (str) and the 
            values are lists of languages (str) of length 3.
    """
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

def make_shorthand_dict(df):
    """
    Create a dictionary using the values of first column as dictionary keys, 
    and the values in other columns as dictionary values.

    Parameters:
        df (pd.DataFrame): A DataFrame containing team full names in the first column
            and their corresponding shorthand names in subsequent columns.

    Return type:
        dict: A dictionary where the keys are team full names (str) and the
            values are their shorthand names (str)
    """
    n = len(df)
    d = {}
    for i in range(0, n):
        name, sh = df.iloc[i]
        d[name] = sh
    return d

def make_standings_dict(df):
    """
    Create a dictionary using the values of first column as dictionary keys, 
    and the values in other columns as dictionary values.

    Parameters:
        d (pd.DataFrame): A DataFrame containing team full names in the first column
            and their corresponding standings in subsequent columns.

    Return type:
        dict: A dictionary where the keys are team full names (str) and the
            values are their standings (int)
    """
    n = len(df)
    d = {}
    for i in range(0, n):
        name, standing = df.iloc[i]
        d[name] = standing
    return d

def map_languages(country, country_dict, current_languages):
    """
    Map a country to its languages and add them to the current list of languages.

    If the country is not found in the country dictionary, a placeholder value 
    ('Country not mapped') is returned. The final list will always have a length of 3.

    Parameters:
        country (str): The name of the country.
        country_dict (dict): A dictionary mapping country names to lists of languages.
        current_languages (list): A list of currently spoken languages.

    Return type:
        list: A list of exactly 3 languages. If the country is found, it returns
            the current languages plus additional languages from the country.
            If not found, it returns 'Country not mapped' or 'NaN' placeholders.
    """
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


def map_role(agents, agent_dct):
    """
    Get the most frequent role for a list of agents from the agent-role dictionary.
    
    Parameters:
        agents (list): A list of agent names
        agent_dict (dict): A dictionary mapping the agent names to playable roles.

    Return type:
        str: The most frequent role among the agents. If the role is not found, 
            it returns 'Not Found' or 'NaN'.
    """
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
    
def map_shorthand(full_name, sh_dict):
    """
    Get the shorthand of a team based on their full name
    
    Parameters:
        full_name (str): Full name of team.
        sh_dict (dict): A dictionary mapping the full names of teams to their shorthand 
            names.

    Return type:
        str: The team's shorthand name. Otherwise, returns 'Team not Mapped' or 'NaN' 
            placeholder.
    """
    if full_name not in sh_dict:
        return 'Team not Mapped'
    return sh_dict[full_name]

def map_standing(full_name, standings_dict):
    """
    Get the highest standing for a team based on their full name.

    Parameters:
        full_name (str): The full name of the team.
        standings_dict (dict): A dictionary mapping team full names to their 
            highest standings achieved.

    Return type:
        str or int: The highest standing if the team is found. If not, returns 
            'Team not Mapped' or 'NaN' as a placeholder.
    """
    if full_name not in standings_dict:
        return 'Team not Mapped'
    return standings_dict[full_name]

def get_table(url, main_lang, role_dict, language_dict, shorthand_dict, standings_dict):
    """
    Extracts a table from the given URL and returns a DataFrame.

    Parameters:
        url (str): The target URL to extract the table from.
        main_lang (list): A list of languages spoken by players in the sub-region.
        role_dict (dict): A dictionary mapping agent names to their roles.
        language_dict (dict): A dictionary mapping country names to lists of languages.
        shorthand_dict (dict): A dictionary mapping team full names to shorthand names.
        standings_dict (dict): A dictionary mapping team full names to their standings.

    Return type:
        pd.DataFrame: A DataFrame containing player data, including columns 
            such as country, team name, roles, and statistics.
    """
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

def get_table_ignore_table(url, main_lang, role_dict, language_dict, shorthand_dict, standings_dict):
    """
    Extracts a table from the given URL and returns a DataFrame, ignoring the first table (if redundant).

    Parameters:
        url (str): The target URL to extract the table from.
        main_lang (list): A list of languages spoken by players in the sub-region.
        role_dict (dict): A dictionary mapping agent names to their roles.
        language_dict (dict): A dictionary mapping country names to lists of languages.
        shorthand_dict (dict): A dictionary mapping team full names to shorthand names.
        standings_dict (dict): A dictionary mapping team full names to their standings.

    Return type:
        pd.DataFrame: A DataFrame containing player data, including their country, team name, role, and other statistics.
    """
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

def merge_subregions(path):
    """
    Merge multiple sub-regions into a single DataFrame, retaining only player entries with the highest standings.

    Parameters:
        path (str): The directory path containing the .csv files for each sub-region.

    Return type:
        pd.DataFrame: A DataFrame containing merged player data from all sub-regions, 
            keeping only entries with the highest standings for each player.
    """
    csv_files = glob.glob(os.path.join(path, '*.csv'))
    dataframes = []
    for file in csv_files:
        sub_region_df = pd.read_csv(file)
        filename = os.path.basename(file)
        sub_region_df['sub_region'] = filename.split('_')[-1].replace('.csv', '')
        dataframes.append(sub_region_df)
    region_df = pd.concat(dataframes, ignore_index = True)
    region_df = region_df.loc[region_df.groupby('ign')['standings'].idxmin()].reset_index(drop = True)
    return region_df