from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

alcDrinks = []
quote_page = "https://en.wikipedia.org/wiki/List_of_alcoholic_drinks"
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
alcohols = soup.find_all('a')
for a in alcohols:
	title = a.get_text()
	if(len(title.split()) <= 2 and len(title.split()) > 0 and title.isalpha() and len(title) > 2):
		alcDrinks.append(title.lower())
alcDrinks.remove('edit')
alcDrinks.remove('edit')
alcDrinks.remove('milk')
alcDrinks.remove('honey')
alcDrinks.remove('corn')
alcDrinks.remove('sugarcane')
alcDrinks = list(set(alcDrinks[4:-19]))
alcDrinks.append('liqueur')
alcDrinks.append('liquor')
alcDrinks.append('triple sec')
alcDrinks.remove('grapes')
alcDrinks.remove('pomegranate')
alcDrinks.remove('juice')
alcDrinks.remove('juices')
alcDrinks.remove('potato')
alcDrinks.remove('pineapples')
alcDrinks.remove('pears')
alcDrinks.remove('rice')
alcDrinks.remove('plums')
alcDrinks.remove('bananas')
alcDrinks.remove('coconut')
alcDrinks.remove('apples')
alcDrinks.remove('sugar')
alcDrinks.remove('distillation')
alcDrinks.remove('apricots')
alcDrinks.remove('ginger')
alcDrinks.remove('agave')
alcDrinks.append('bitters')
alcDrinks.append('rumchata')
alcDrinks.append('amaretto')
alcDrinks.append('irish cream')
alcDrinks.append('schnapps')
alcDrinks.append('grain alcohol')

for i in range(len(alcDrinks)):
	alcDrinks[i] = re.sub(r'[^\x00-\x7F]+',' ', alcDrinks[i])

garnish = ['olive', "cucumber", 'peppermint', "choco", "chocolate", "tobasco", "syrup", 'wedge', 'whipped cream', "caramel", 'vanilla extract', 'wedges', 'nutmeg', 'pepper', 'celery', 'salt', 'cinnamon', 'vanilla', 'ice', 'sugar', 'sugarcane']
fruit = ['cranberry', 'coconut', 'mango', 'limes', 'cherry', 'lime', 'pineapple', 'melon', "watermelon", 'pear', 'strawberry', 'lemon', 'apple', 'gava', 'orange', 'banana', 'grape', 'pinapples', 'grapes', 'grapefruit', 'pomegranate']
nonAlc = ['sprite', 'coke', 'coca', 'cola', 'soda', 'sparkling', 'ginger ale', 'milk', 'coffee']
juice = []
for x in fruit:
	juice.append(x + " " + "juice")

print(alcDrinks)
print(garnish)
print(fruit)
print(nonAlc)
print(juice)

with open('alcDrinks.csv', 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(alcDrinks)

with open('fruit.csv', 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(fruit)

with open('juice.csv', 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(juice)

with open('garnish.csv', 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(garnish)

with open('nonAlc.csv', 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(nonAlc)