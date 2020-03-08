import requests
from bs4 import BeautifulSoup
import numpy as np

def convertDigit(string):
    if string.replace(",", "").isdigit():
        return int(string.replace(",", ""))
    return string

url = 'https://www.worldometers.info/coronavirus/#countries'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser") # Parse html

table = soup.find("table", {"id": "main_table_countries"}).find_all("tbody") # table
tr_elems = table[0].find_all("tr") # All rows in table

data = []
for tr in tr_elems: # Loop through rows
    td_elems = tr.find_all("td") # Each collumn in row
    data.append([convertDigit(td.text.strip()) for td in td_elems])

np_array = np.array(data)



print(np_array)
#rudri was here
