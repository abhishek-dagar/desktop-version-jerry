from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
import os
import re


def down_movie(movie_name1):
    movie_name = movie_name1.replace(" ", "+")
    url = "https://torrentz2eu.net/search.php?q=" + movie_name
    url = Request(url, headers={'User-Agent': 'Google Chrome'})
    try:
        response = urlopen(url)
    except:
        return "movie not found"
        pass
    html = response.read()
    soup1 = soup(html, "lxml")
    url_list = []
    links = soup1.find_all('a')

    divs = soup1.find_all("table", {"class": "table table-responsive table-bordered table-striped"})
    size_list = []
    for div in divs:
        row = ''
        rows = div.findAll('td')
        for row in rows:
            if row['data-title'] == "Size":
                row = row.text
                row1 = ""
                if "GB" in row:
                    for i in row:
                        if i.isdigit() or i == ".":
                            row1 = row1 + i
                    row = row1
                size_list.append(row)

    i = 0
    for link in links:
        movie_name2 = movie_name1.split(" ")
        if movie_name2[0] in link['href'].lower():
            url_list.append(link['href'])
    
    dict = {}
    size_list1 = []
    url_list2 = []
    for i in range(len(url_list)):
        if "MB" not in size_list[i]:
            ro = round(float(size_list[i]))
        if "MB" in size_list[i]:
            dict[size_list[i]] = url_list[i]
            size_list1.append(size_list[i])
            url_list2.append(url_list[i])
        elif ro < 3:
            dict[size_list[i]] = url_list[i]
            size_list1.append(size_list[i])
            url_list2.append(url_list[i])



    url_name = []
    for i in range(len(dict)):
        ch = dict[size_list1[i]]
        ch = ch.split("=")
        url_name.append(ch[2])
    return url_name, url_list2

