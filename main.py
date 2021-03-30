import requests
from bs4 import BeautifulSoup
from contextlib import redirect_stdout


page = requests.get("https://www.newegg.com/p/pl?N=100007709%20601341679%208000%20600007308%20600007306%20601296707%20601331379%20601357282%20601359511&PageSize=96")
soup = BeautifulSoup(page.text, 'html.parser')

page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')

divTag = soup.find_all("div", {"class": "item-container"})

for tag in divTag:
    tdTags = tag.select("button", {"class": "btn-primary"})
    print(tdTags[0].contents, tdTags[0].parent.parent.parent.parent.contents[0])




with open('./myfile.txt', 'w') as f:
    with redirect_stdout(f):
        print(tdTags[0].contents, tdTags[0].parent.parent.parent.parent.contents[0])