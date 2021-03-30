import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df

page = requests.get("https://www.newegg.com/p/pl?N=100007709%20601357282%20601321572%20601359511%20601341679")
soup = BeautifulSoup(page.text, 'html.parser')


page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')

item_tree_list = soup.find_all(class_ = 'btn btn-primary btn-mini')
for i in item_tree_list[:4]:
  print(i)


links = soup.find_all(class_ = 'item-title')
for i in links[:4]:
  print(i)

if not item_tree_list:
    print("nothing")

if item_tree_list:
    print("something in stock")
