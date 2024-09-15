from bs4 import BeautifulSoup
import requests

def get_player_urls(player_html_text):
    player_urls = []
    for text in player_html_text:
        value = text.find('a', class_ = False)
        if value != None:
            player_urls.append(value['href'])
    return player_urls

def get_player_names(player_html_text):
    player_names = []
    for text in player_html_text:
        value = text.find('a', class_ = False)
        if value != None:
            player_names.append(value['title'])
    return player_names

# To be implemented
def player_scrape(player_url, field):
    base_url = 'https://liquipedia.net'
    site_url = base_url + player_url + field
    request = requests.get(site_url)
    player_soup = BeautifulSoup(request.text, 'html.parser')
    
    text_scrape = player_soup.find_all('th')
    headers = [title.text for title in text_scrape]
    
    statistics_scrape = player_soup.find_all('th')
    statistics = statistics_scrape # to be impleme
    return headers, statistics