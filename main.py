import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://www.newegg.com/p/pl?N=100007709%20601341679%20600007308%20600007306%20601296707%20601331379%20601357282%20601359511%20600286767%20600083901%20600007320%20600007315&PageSize=96")
soup = BeautifulSoup(page.text, 'html.parser')

page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')

divTag = soup.find_all("div", {"class": "item-container"})

candidates = set()
want = {'550', '3070'}
for tag in divTag:
    tdTags = tag.select("button", {"class": "btn-primary"})
    tag_contents = tdTags[0].contents
    if 'View Details' in str(tag_contents[0]):
        continue
    tag_link = tdTags[0].parent.parent.parent.parent.contents[0]
    for wanted in want:
        if wanted in tag_link.attrs['href']:
            candidates.add(tag_link)

print(candidates)
