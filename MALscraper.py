# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import selenium

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

URL = 'https://myanimelist.net/topanime.php'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='content')

anime_elems = results.find_all('tr', class_='ranking-list')

rows = []

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
    







