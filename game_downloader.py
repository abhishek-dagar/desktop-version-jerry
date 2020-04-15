from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
import os

def game_name(game_name1):
    game_name = game_name1.replace(" ", "+")
    url = "http://oceanofgames.com/?s=" + game_name
    url = Request(url, headers={'User-Agent': 'Google Chrome'})
    try:
        response = urlopen(url)
    except:
        print("game not found")
        pass
    html = response.read()
    soup1 = soup(html, "lxml")
    url_list = []
    url_name = []
    links = soup1.find_all('a')
    for link in links:
        game_name = game_name1.split(" ")
        if game_name[0] in link['href']:
            link = link['href']
            sp = link.split('/')
            if game_name[0] in sp[3]:
                url_list.append(link)
                url_name.append(sp[3])
    return url_name,url_list






