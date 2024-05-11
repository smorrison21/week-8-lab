#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?

#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import requests
from bs4 import BeautifulSoup
#web to python
url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path = r'/Users/sarahmorrison/Downloads/GitHub/week-8-lab/lab 8b table.csv'
response = requests.get(url)

#from wholeto table
soup = BeautifulSoup(response.text, 'lxml')
tables = soup.find_all('table')
print(len(tables))
print('Madonna' in tables[0].text)

#tabel to lists of rows and cells
table = tables[0]
rows = table.find_all('tr')
#r for r in rows
cells = [r.find_all(lambda c: c.name in ['td', 'th']) for r in rows]
#from raw content to csv suitable content
text = [[t.text.strip().replace('\n', ' ').replace(',','') for t in c] for c in cells]

with open(path, 'w') as ofile:
    ofile.write(text)