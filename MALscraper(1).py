
from bs4 import BeautifulSoup
import pandas as pd
import requests

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

URL = 'https://myanimelist.net/topanime.php'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')

results = soup.find(id='content')

table = results.find_all('table')[0] 
df = pd.read_html(str(table))
print(df)

# rows = []

# for anime in anime_elems:
#     rank_elems = anime.find('td', class_='rank ac')
#     title_elems = anime.find('div', class_='di-ib clearfix')
#     score_elems = anime.find('td', class_='score ac fs14')
#     if None in (rank_elems, title_elems, score_elems):
#         continue
#     print("Rank:", rank_elems.text.strip())
#     print("Title:", title_elems.text.strip())
#     print("Score:", score_elems.text.strip())
#     print()