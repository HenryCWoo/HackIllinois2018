from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import numpy as np

def getFeatVect2(url):

	def string_found(string1, string2):
	   if re.search(r"\b" + re.escape(string1) + r"\b", string2):
	      return True
	   return False

	alcDrinks = []
	fruit = []
	juice = []
	garnish = []
	nonAlc = []

	with open('alcDrinks.csv', 'r') as f:
	    reader = csv.reader(f)
	    alcDrinks = list(reader)
	with open('fruit.csv', 'r') as f:
	    reader = csv.reader(f)
	    fruit = list(reader)
	with open('juice.csv', 'r') as f:
	    reader = csv.reader(f)
	    juice = list(reader)
	with open('garnish.csv', 'r') as f:
	    reader = csv.reader(f)
	    garnish = list(reader)
	with open('nonAlc.csv', 'r') as f:
	    reader = csv.reader(f)
	    nonAlc = list(reader)

	alcDrinks = alcDrinks[0]
	fruit = fruit[0]
	juice = juice[0]
	garnish = garnish[0]
	nonAlc = nonAlc[0]

	quote_page = url
	# query the website and return the html to the variable ‘page’
	page = urlopen(quote_page)
	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')
	# get the index price
	name = soup.find('h1').text
	# print(name)
	# Take out the <div> of name and get its value
	ingredients = []
	for ingred in soup.find_all('td', class_='normal2'):
		for i in ingred.find_all('u'):
			ingredients.append(i.text) 

	rating = float(soup.find_all("span", {'class':"important2gras"})[1].text)/4
	# print(rating)

	nonAlcs = []
	alcohols = []
	fruits = []
	garnishes = []
	juices = []

	def featAppend(feature, elem, column):
		if(sum(1 for x in feature[0][column] if x > 0) >= 4):
			return
		else:
			i = 0
			while(feature[0][column][i] != 0):
				i+=1
			feature[0][column][i] = elem

	feature = [[[0]*4,[0]*4,[0]*4,[0]*4,[0]*4], float(rating), name]
	flag = 0
	for i in ingredients:
		for j in alcDrinks:
			if(string_found(j, i.lower())):
				flag = 1
				featAppend(feature, alcDrinks.index(j), 0)
				alcohols.append(i)
				break
		if(flag != 1):
			for j in juice:
				if(string_found(j, i.lower())):
					flag = 1
					featAppend(feature, juice.index(j), 1)
					juices.append(i)
					break
		if(flag != 1):
			for j in garnish:
				if(string_found(j, i.lower())):
					flag = 1
					garnishes.append(i)
					featAppend(feature, garnish.index(j), 2)
					break
		if(flag != 1):
			for j in fruit:
				if(string_found(j, i.lower())):
					flag = 1
					fruits.append(i)
					featAppend(feature, fruit.index(j), 3)
					break
		if(flag != 1):
			for j in nonAlc:
				if(string_found(j, i.lower())):
					flag = 1
					nonAlcs.append(i)
					featAppend(feature, nonAlc.index(j), 4)
					break
		
		flag = 0


	# print("alcohol", alcohols) 
	# print("nonalc",nonAlc) 
	# print("juices",juices) 
	# print("garn",garnishes)
	# print("fruits",fruits)
	feature[0] = list(np.array(feature[0]).flatten())
	# print(feature)
	return feature