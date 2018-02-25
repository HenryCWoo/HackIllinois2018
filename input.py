# Get user input to predict
import numpy as np
import random

alcohol = ['boza', 'tsikoudia', 'williamine', 'orujo', 'lager', 'tequila', 'aila', 'piscos', 'kasikisi', 'tongba', 'urgwagwa', 'armagnac', 'feni', 'tescovin ', 'cocoroco', 'ale', 'tonto', ' uic ', 'dunjeva a', 't rk lyp linka', 'pomace', 'palm', 'damassine', 'korn', 'molasses', 'whiskey', 'sorghum', 'horilka', 'bilibili', 'cacha a', 'plantains', 'toddy', 'umeshu', 'bock', 'arak', 'tiswin', 'burukutu', 'sake', 'rakia', 'apfelwein', 'brandy', 'okolehao', 'wheat', 'tepache', 'pilsener', 'aguardiente', 'vodka', 'soju', ' uic ', 'perry', 'marsala', 'cassava', 'tembo', 'edit', 'guaro', 'tesguino', 'huangjiu', 'schnapps', 'pisco', 'baijiu', 'cognac', 'tiquira', 'thwon', 'applejack', 'makgeolli', 'merisa', 'stout', 'rak ', 'barley', 'obstwasser', 'tequilas', 'zivania', 'pito', 'rye', 'tuak', 'cashew', 'buckwheat', 'trester', 'sonti', 'vinjak', 'lozova a', 'borovi ka', 'akvavit', 'pinga', 'ouzo', 'absinthe', 'vodkas', 'rum', 'gin', 'parakari', 'wine', 'shochu', 'sahti', ' ljivovica', 'tsipouro', 'kirsch', 'madeira', 'millet', 'quinces', 'jabukova a', 'mamajuana', 'mbege', 'palinka', 'marc', 'clairin', 'brem', 'kvass', 'beer', 'cider', 'ogogoro', 'moonshine', 'witbier', 'kajsijeva a', 'maotai', 'choujiu', 'grappa', 'pastis', 'cauim', 'chungju', 'poir ', 'awamori', 'beers', 'blaand', 'majmunova a', 'highball', 'pulque', 'wines', 'ethanol', 'metaxa', 'mezcal', 'viljamovka', 'cocktails', 'kumis', 'singani', 'fermenting', 'kilju', 'gouqi', 'port', 'spirits', 'himbeergeist', 'nihamanchi', 'kasiri', 'whisky', 'porter', 'tej', 'vinsanto', 'mead', 'jenever', 'schwarzbier', 'vermouth', 'arrack', 'raki', 'basi', 'slivovitz', 'kefir', 'sangria', 'chicha', 'liqueurs', 'barleywine', 'calvados', 'sambuca', 'champagne', 'raicilla', 'poit n', 'sherry', 'baga o', 'p linka', 'liqueur', 'liquor', 'triple sec', 'bitters', 'rumchata', 'amaretto', 'irish cream', 'schnapps', 'grain alcohol']
garnish = ['olive', 'cucumber', 'peppermint', 'choco', 'chocolate', 'tobasco', 'syrup', 'wedge', 'whipped cream', 'caramel', 'vanilla extract', 'wedges', 'nutmeg', 'pepper', 'celery', 'salt', 'cinnamon', 'vanilla', 'ice', 'sugar', 'sugarcane']
fruits = ['cranberry', 'coconut', 'mango', 'limes', 'cherry', 'lime', 'pineapple', 'melon', 'watermelon', 'pear', 'strawberry', 'lemon', 'apple', 'gava', 'orange', 'banana', 'grape', 'pinapples', 'grapes', 'grapefruit', 'pomegranate']
nonAlcs = ['sprite', 'coke', 'coca', 'cola', 'soda', 'sparkling', 'ginger ale', 'milk', 'coffee']
juice = ['cranberry juice', 'coconut juice', 'mango juice', 'limes juice', 'cherry juice', 'lime juice', 'pineapple juice', 'melon juice', 'watermelon juice', 'pear juice', 'strawberry juice', 'lemon juice', 'apple juice', 'gava juice', 'orange juice', 'banana juice', 'grape juice', 'pinapples juice', 'grapes juice', 'grapefruit juice', 'pomegranate juice']

# Input from user looks like this
# [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2, 3)]
#	alc		alc		alc		alc		other

# Need to come up with list
# [1, 2, 3, 4, 5]

ingredients = [[0] for i in range(5)]

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
	for j in range(4):
		if(j < len(ingredients[0])):
			r = random.randint(0, len(ingredients[0]))
			if(ingredients[0][r] not in potential[i]):
				potential[i].append(ingredients[0][r])
		else:
			potential[i].append(0)  

	for j in range(4):
		if(j < len(ingredients[1])):
			r = random.randint(0, len(ingredients[1]))
			if ingredients[1][r] not in potential[i]:
				potential[i].append(ingredients[1][r])
		else:
			potential[i].append(0)  


	for j in range(4):
		if(j < len(ingredients[2])):
			r = random.randint(0, len(ingredients[2]))
			if ingredients[2][r] not in potential[i]:
				potential[i].append(ingredients[2][r])
		else:
			potential[i].append(0)  


	for j in range(4):
		if(j < len(ingredients[3])):
			r = random.randint(0, len(ingredients[3]))
			if ingredients[3][r] not in potential[i]:
				potential[i].append(ingredients[3][r]) 
		else:
			potential[i].append(0)  


	for j in range(4):
		if(j < len(ingredients[4])):
			r = random.randint(0, len(ingredients[4]))
			if ingredients[4][r] not in potential[i]:
				potential[i].append(ingredients[4][r]) 
		else:
			potential[i].append(0)  
