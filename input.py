# Get user input to predict
import numpy as np
import random
from keras.models import load_model

alcohol = ['boza', 'tsikoudia', 'williamine', 'orujo', 'lager', 'tequila', 'aila', 'piscos', 'kasikisi', 'tongba', 'urgwagwa', 'armagnac', 'feni', 'tescovin ', 'cocoroco', 'ale', 'tonto', ' uic ', 'dunjeva a', 't rk lyp linka', 'pomace', 'palm', 'damassine', 'korn', 'molasses', 'whiskey', 'sorghum', 'horilka', 'bilibili', 'cacha a', 'plantains', 'toddy', 'umeshu', 'bock', 'arak', 'tiswin', 'burukutu', 'sake', 'rakia', 'apfelwein', 'brandy', 'okolehao', 'wheat', 'tepache', 'pilsener', 'aguardiente', 'vodka', 'soju', ' uic ', 'perry', 'marsala', 'cassava', 'tembo', 'edit', 'guaro', 'tesguino', 'huangjiu', 'schnapps', 'pisco', 'baijiu', 'cognac', 'tiquira', 'thwon', 'applejack', 'makgeolli', 'merisa', 'stout', 'rak ', 'barley', 'obstwasser', 'tequilas', 'zivania', 'pito', 'rye', 'tuak', 'cashew', 'buckwheat', 'trester', 'sonti', 'vinjak', 'lozova a', 'borovi ka', 'akvavit', 'pinga', 'ouzo', 'absinthe', 'vodkas', 'rum', 'gin', 'parakari', 'wine', 'shochu', 'sahti', ' ljivovica', 'tsipouro', 'kirsch', 'madeira', 'millet', 'quinces', 'jabukova a', 'mamajuana', 'mbege', 'palinka', 'marc', 'clairin', 'brem', 'kvass', 'beer', 'cider', 'ogogoro', 'moonshine', 'witbier', 'kajsijeva a', 'maotai', 'choujiu', 'grappa', 'pastis', 'cauim', 'chungju', 'poir ', 'awamori', 'beers', 'blaand', 'majmunova a', 'highball', 'pulque', 'wines', 'ethanol', 'metaxa', 'mezcal', 'viljamovka', 'cocktails', 'kumis', 'singani', 'fermenting', 'kilju', 'gouqi', 'port', 'spirits', 'himbeergeist', 'nihamanchi', 'kasiri', 'whisky', 'porter', 'tej', 'vinsanto', 'mead', 'jenever', 'schwarzbier', 'vermouth', 'arrack', 'raki', 'basi', 'slivovitz', 'kefir', 'sangria', 'chicha', 'liqueurs', 'barleywine', 'calvados', 'sambuca', 'champagne', 'raicilla', 'poit n', 'sherry', 'baga o', 'p linka', 'liqueur', 'liquor', 'triple sec', 'bitters', 'rumchata', 'amaretto', 'irish cream', 'schnapps', 'grain alcohol']
garnish = ['olive', 'cucumber', 'peppermint', 'choco', 'chocolate', 'tobasco', 'syrup', 'wedge', 'whipped cream', 'caramel', 'vanilla extract', 'wedges', 'nutmeg', 'pepper', 'celery', 'salt', 'cinnamon', 'vanilla', 'ice', 'sugar', 'sugarcane']
fruits = ['cranberry', 'coconut', 'mango', 'limes', 'cherry', 'lime', 'pineapple', 'melon', 'watermelon', 'pear', 'strawberry', 'lemon', 'apple', 'gava', 'orange', 'banana', 'grape', 'pinapples', 'grapes', 'grapefruit', 'pomegranate']
nonAlcs = ['sprite', 'coke', 'coca', 'cola', 'soda', 'sparkling', 'ginger ale', 'milk', 'coffee']
juice = ['cranberry juice', 'coconut juice', 'mango juice', 'limes juice', 'cherry juice', 'lime juice', 'pineapple juice', 'melon juice', 'watermelon juice', 'pear juice', 'strawberry juice', 'lemon juice', 'apple juice', 'gava juice', 'orange juice', 'banana juice', 'grape juice', 'pinapples juice', 'grapes juice', 'grapefruit juice', 'pomegranate juice']

def randChoose(choose):
	return random.randint(0, len(choose)-1)

def fillCat(cat, mod):
	fill = []
	for n in range(4):
		if(n < len(cat)):
			flag = True
			while(flag):
				rand = cat[randChoose(cat)]
				if(rand not in fill):
					flag = False
					fill.append(rand)
		else:
			fill.append(0)
	for n in fill:
		mod.append(n)

def codeToFood(code, cat):
	return print(cat[code] + '\n')

def printFood(ingredients):
	for n in range(len(ingredients)):
		if(n < 4):
			codeToFood(i, alcohol)
		elif(n < 8):
			codeToFood(i, garnish)
		elif(n < 12):
			codeToFood(i, fruits)
		elif(n < 16):
			codeToFood(i, nonAlcs)
		else:
			codeToFood(i, juice)
		n += 1

# Input from user looks like this
# [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2, 3)]
#	alc		alc		alc		alc		other

# Need to come up with list
# [1, 2, 3, 4, 5]

# ingredients = [[0] for i in range(5)]
ingredients = [[5, 8, 54], [1, 4, 5], [4, 6, 12], [3, 5, 9], [2, 5, 21]]



alcohol = [np.zeros(()) for i in range(4)]
garnish = [np.zeros(()) for i in range(4)]
fruits  = [np.zeros(()) for i in range(4)]
nonAlc  = [np.zeros(()) for i in range(4)]
juice	= [np.zeros(()) for i in range(4)]

base = 1

for i in ingredients:
	if(len(i) != 0):
		base *= len(i)

potential = [[] for i in range(base)]
print(potential)

for i in range(base):
	for j in range(5):
		fillCat(ingredients[j], potential[i])


print(potential)

model = load_model('basisDecision.h5')

maxResult = 0

for test in potential:
	curr = model.predict(np.array(test))
	if(curr > maxResult):
		maxResult = curr
		bestIngredients = np.array(test)


print('Our Predicted Score: ', maxResult)
printFood(bestIngredients)	
