import re
import sys
import time
from tkinter import *
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager


window = Tk()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.youtube.com/watch?v=AWYFxoAUUSM")
i = 0
arr = []
while i < 40:
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i+1
    print(i)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
block_tag = soup.select_one('#contents')
for link in soup.find_all('a', {"class": "yt-simple-endpoint style-scope ytd-compact-video-renderer"}):
    link_a = link.get('href')
    if link_a != None and link_a != "/" and link_a != "":
        arr.append("https://www.youtube.com"+link_a)
        print(link_a)
f = open("myfile.json", "w")
y = json.dumps(arr)
f.write(y)
f.close()

driver.quit()
