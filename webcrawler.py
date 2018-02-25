import numpy as np
from bs4 import BeautifulSoup
import re
from collections import deque
from urllib.request import urlopen
import time

exec(open('sorter.py').read())
exec(open('sorter2.py').read())

def unique(convert):    
    return re.findall('/([0-9^"]*)/', convert)[1]

def uniqueSec(convert):    
    return re.findall('/([0-9^"]*)/', convert)[0]

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
                 'http://allrecipes.com/recipe/158307/',

                 'http://allrecipes.com/recipe/32232/',
                 'http://allrecipes.com/recipe/23534/',
                 'http://allrecipes.com/recipe/17770/',
                 'http://allrecipes.com/recipe/218330/',
                 'http://allrecipes.com/recipe/32451/',
                 'http://allrecipes.com/recipe/23034/',
                 'http://allrecipes.com/recipe/20213/',
                 'http://allrecipes.com/recipe/20574/',
                 'http://allrecipes.com/recipe/53525/',
                 'http://allrecipes.com/recipe/235346/',
                 'http://allrecipes.com/recipe/34761/',
                 'http://allrecipes.com/recipe/9472/',
                 'http://allrecipes.com/recipe/96761/',
                 'http://allrecipes.com/recipe/32232/',
                 'http://allrecipes.com/recipe/159004/',
                 'http://allrecipes.com/recipe/215834/',
                 'http://allrecipes.com/recipe/220481/',
                 'http://allrecipes.com/recipe/235010/',
                 'http://allrecipes.com/recipe/230311/'])

f = open('DaBestResults.txt', 'a')

while(len(queue) > 0):
    quote_page = queue.popleft()

    uniqueN = unique(quote_page)
    if(visited[int(uniqueN)] == 1):
        continue
    else:
        visited[int(uniqueN)] = 1

    html = urlopen(quote_page)
    match = BeautifulSoup(html, 'html.parser')
    
    for div in match.find_all('div', class_='slider-card__recipes'):
        address = div.a['href']
        addrNum = unique(address)
        visited[int(addrNum)] = 1
        queue.append(address)
        print(address)
        time.sleep(1)
        f.write(str(getFeatVect(address)) + '\n')

visited = np.zeros(max_index)

# Browse new recipes
base = "http://www.1001cocktails.com/recipes/cocktails/cocktails_list_vu.php3?&start="
offset = 100

for mult in range(10, 110):
    # Get the current index page
    curr = base + str(offset * mult)

    # Get the html for index page
    html = urlopen(curr)
    match = BeautifulSoup(html, 'html.parser')

    for recipe in match.find_all('div'):
        for i in recipe.find_all('a'):
            if(bool(re.search('/([0-9^"].*)/',i['href'])) and (visited[int(uniqueSec(i['href']))] == 0)):
                print('http://www.1001cocktails.com' + i['href'])
                time.sleep(2)
                f.write(str(getFeatVect2('http://www.1001cocktails.com' + i['href'])) + '\n')
                visited[int(uniqueSec(i['href']))] = 1
