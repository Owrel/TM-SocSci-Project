import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
import time
import os


data = pd.read_csv('./DeSmog_data.csv')

url = 'https://www.desmogblog.com/tony-abbott'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('a')
for l in links :
    if l.get('href') != None :
        if 'twitter' in l.get('href'):
            if 'https://twitter.com/DeSmogBlog' != l.get('href'):
                print(l.get('href'))


twitter_links = []
# Iterating over the all of the DeSmogBlog page
for index in range(len(data['link DeSmogBlog'])):
    time.sleep(1)
    print(f"Scrapping : {index}/{len(data['link DeSmogBlog'])-1}")
    # print(data['link DeSmogBlog'][index])
    # Get url 
    url = data['link DeSmogBlog'][index]
    page = requests.get(url) # Scrapping the page
    soup = BeautifulSoup(page.content, 'html.parser') # Soup will make the html page easier to read
    links = soup.find_all('a') # get all <a></a>
    for l in links :
        if l.get('href') != None : # get all <a></a> that contain href attribute
            if 'twitter' in l.get('href'): # get the link that contain twitter
                if 'https://twitter.com/DeSmogBlog' != l.get('href'):
                    # print(l.get('href'))
                    if not l.get('href') in twitter_links:
                        twitter_links.append(l.get('href'))

"""
Writing all of the twitter link in a doc file
"""
file = open('twitter_link.txt', 'a')

for t in twitter_links :
    file.write('\n' + t)
file.close()






