#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import winsound
import random
#config options
options = webdriver.ChromeOptions()
options.headless = True
followS = ""
followI = 0
followIO = 0
#set the URL you want to webscrape from
url = 'https://tokcount.com/?user=mrsam993'
#connect to the URL
browser = webdriver.Chrome(options=options, executable_path='D:\chromedriver')
browser.get(url)
#find and print relevent data
while True:
    #let the website load
    time.sleep(5)
    #parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(browser.page_source, "html.parser")
    #get follower count
    for i in range(4):
        links = soup.findAll('span', class_= 'odometer-value') [i]
        followS += str(links)[29]
    #convert the follow count to an int
    followI = int(followS)
    #if there was an increase play a sound
    if followIO != followI:
        winsound.PlaySound("1 (1)", winsound.SND_FILENAME)
    #update follow old
    followIO = followI
    #reset the follower string
    followS = ""
