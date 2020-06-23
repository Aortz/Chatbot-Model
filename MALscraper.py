# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://myanimelist.net/topanime.php'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='content')

anime_elems = results.find_all('tr', class_='ranking-list')

for anime in anime_elems:
    rank_elems = anime.find('td', class_='rank ac')
    title_elems = anime.find('div', class_='di-ib clearfix')
    score_elems = anime.find('td', class_='score ac fs14')
    if None in (rank_elems, title_elems, score_elems):
        continue
    print("Rank:", rank_elems.text.strip())
    print("Title:", title_elems.text.strip())
    print("Score:", score_elems.text.strip())
    print()
    