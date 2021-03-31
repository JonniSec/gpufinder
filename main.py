import discord
import asyncio
import requests
import re
from bs4 import BeautifulSoup
from contextlib import redirect_stdout
import time

def gpufunction(): # function to see if gpus are available and stores into a list

    page = requests.get("https://www.newegg.com/p/pl?N=100007709%20601341679%208000%20600007308%20600007306%20601296707%20601331379%20601357282%20601359511&PageSize=96") # grab gpu page

    page.encoding = 'ISO-885901'

    soup = BeautifulSoup(page.text, 'html.parser') # parse html

    divTags = soup.find_all("div", {"class": "item-container"})

    availableList = [] # empty list to store gpus that can be bought

    for tag in divTags:
        tdTags = tag.select("button", {"class": "btn-primary"})
        # print(tdTags[0].contents)
        tdTagKid = tdTags[0].parent.parent.parent.parent.contents[0] # grabs location of url from Tag object
        if 'Add to cart ' in tdTags[0].contents:
            # print('Available item: '  + tdTagKid.attrs['href'])
            availableList.append(tdTagKid.attrs['href']) # pulls url out of Tag object


    # with open('./myfile.txt', 'w') as f:
    #     with redirect_stdout(f):
    #         for i in availableList:
    #             print(i)
    return availableList


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())
        self.previousavailable = []

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        nowavailable = gpufunction() # stores available gpus into empty list
        #print(nowavailable)

        if nowavailable != self.previousavailable: # if there is a change in available gpus in newegg
            channel = self.get_channel(761812096496304132) # channel ID

            for i in nowavailable:
                await channel.send (i) # print available gpus to discord
                time.sleep(1)

            await asyncio.sleep(300) # task runs every 5 minutes
        # while not self.is_closed():
            self.previousavailable = nowavailable # set available gpus to previous for next comparison

client = MyClient()
client.run('TOKEN')

