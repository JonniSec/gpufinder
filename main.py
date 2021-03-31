import requests
import re
from bs4 import BeautifulSoup
from contextlib import redirect_stdout


page = requests.get("https://www.newegg.com/p/pl?N=100007709%20601341679%208000%20600007308%20600007306%20601296707%20601331379%20601357282%20601359511%201065807788%201065806685%201065826556%201065717567%201065535553%201065528269%201065695668&PageSize=96")

page.encoding = 'ISO-885901'

soup = BeautifulSoup(page.text, 'html.parser')

divTags = soup.find_all("div", {"class": "item-container"})

availableList = []

for tag in divTags:
    tdTags = tag.select("button", {"class": "btn-primary"})
    # print(tdTags[0].contents)
    tdTagKid = tdTags[0].parent.parent.parent.parent.contents[0]
    if 'Add to cart ' in tdTags[0].contents:
        # print('Available item: '  + tdTagKid.attrs['href'])
        availableList.append(tdTagKid.attrs['href'])


with open('./myfile.txt', 'w') as f:
    with redirect_stdout(f):
        for i in availableList:
            print(i)