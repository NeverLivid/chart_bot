from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")

browser= webdriver.Chrome('/Users/paytontaylor/opt/anaconda3/lib/python3.8/site-packages/chromedriver_binary/chromedriver')

message = '!chart daily TSM'

cmnd_split = message.split(' ')
ticker = cmnd_split[2]


browser.get('https://finviz.com/')
inpt = browser.find_element_by_xpath("//*[@id=\"search\"]/div/form/input")
inpt.send_keys(ticker)

search_buttoon = browser.find_element_by_xpath("//*[@id=\"search\"]/div/form/span")
search_buttoon.click()

publish_button = browser.find_element_by_class_name('tab-link')
publish_button.click()

page = browser.page_source
soup = BeautifulSoup(page)

browser.close()

chart_url = soup.find('img', {'alt': 'Finviz Chart'})
chart_url = str(chart_url)
chart_url = chart_url.split('\"')
chart_url = chart_url[3]