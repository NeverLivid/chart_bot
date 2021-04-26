import discord
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

TOKEN = 'ODI1MjEzNjk3ODQwNTEzMDY2.YF6qJQ._fOUzX_lhPTTVGd8gr5fio_zL30'

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'
          .format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!chart daily'):
        cmnd_split = str(message.content)
        cmnd_split = cmnd_split.split(' ')

        ticker = cmnd_split[2]
        print(ticker)

        # await message.channel.send(ticker)

        browser = webdriver.Chrome('/Users/paytontaylor/opt/anaconda3/lib/python3.8/site-packages/chromedriver_binary/chromedriver',
                                   options=chrome_options )
        browser.get('https://finviz.com/quote.ashx?t=' + ticker)

        publish_button = browser.find_element_by_class_name('tab-link')
        publish_button.click()

        page = browser.page_source
        soup = BeautifulSoup(page)

        browser.close()

        chart_url = soup.find('img', {'alt': 'Finviz Chart'})
        chart_url = str(chart_url)
        chart_url = chart_url.split('\"')
        chart_url = chart_url[2]

        await message.channel.send(chart_url)


client.run(TOKEN)

