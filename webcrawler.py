import numpy as np
from bs4 import BeautifulSoup
import re
from collections import deque
from urllib.request import urlopen
import time

exec(open('sorter.py').read())

max_index = 1000000

visited = np.zeros(max_index)

queue = deque([  'http://allrecipes.com/recipe/18936/',
                 'http://allrecipes.com/recipe/136514/',
                 'http://allrecipes.com/recipe/20132/',
                 'http://allrecipes.com/recipe/215615/',
                 'http://allrecipes.com/recipe/42713/',
                 'http://allrecipes.com/recipes/1743/',
                 'http://allrecipes.com/recipe/158307/',
                 'http://allrecipes.com/recipe/222411/',
                 'http://allrecipes.com/recipe/162397/',
                 'http://allrecipes.com/recipe/222419/',
                 'http://allrecipes.com/recipe/245265/',
                 'http://allrecipes.com/recipe/83944/',
                 'http://allrecipes.com/recipe/215615/',
                 'http://allrecipes.com/recipe/221893/',
                 'http://allrecipes.com/recipe/232389/',
                 'http://allrecipes.com/recipe/74971/',
                 'http://allrecipes.com/recipe/23080/',
                 'http://allrecipes.com/recipe/163121/',
                 'http://allrecipes.com/recipe/163141/',
                 'http://allrecipes.com/recipe/158307/'])

addr = []
for i in queue:
    # print(re.findall('/([0-9^"]*)/', i)[1])
    addr.append(re.findall('/([0-9^"]*)/', i)[1])

for num in addr:
    visited[int(num)] = 1


f = open('results.txt', 'a')

while(len(queue) > 0):
    quote_page = queue.popleft()

    html = urlopen(quote_page)
    match = BeautifulSoup(html, 'html.parser')
    
    for div in match.find_all('div', class_='slider-card__recipes'):
        address = div.a['href']
        addrNum = re.findall('/([0-9^"]*)/', address)[1]
        visited[int(addrNum)] = 1
        queue.append(address)
        print(address)
        time.sleep(1)
        f.write(str(getFeatVect(address)) + '\n')

def unique(link):    
    return int(re.findall)
#     print(link.get('data-ratingstars'))

