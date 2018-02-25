import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import ast
from keras.models import load_model

alcohol = ['boza', 'tsikoudia', 'williamine', 'orujo', 'lager', 'tequila', 'aila', 'piscos', 'kasikisi', 'tongba', 'urgwagwa', 'armagnac', 'feni', 'tescovin ', 'cocoroco', 'ale', 'tonto', ' uic ', 'dunjeva a', 't rk lyp linka', 'pomace', 'palm', 'damassine', 'korn', 'molasses', 'whiskey', 'sorghum', 'horilka', 'bilibili', 'cacha a', 'plantains', 'toddy', 'umeshu', 'bock', 'arak', 'tiswin', 'burukutu', 'sake', 'rakia', 'apfelwein', 'brandy', 'okolehao', 'wheat', 'tepache', 'pilsener', 'aguardiente', 'vodka', 'soju', ' uic ', 'perry', 'marsala', 'cassava', 'tembo', 'edit', 'guaro', 'tesguino', 'huangjiu', 'schnapps', 'pisco', 'baijiu', 'cognac', 'tiquira', 'thwon', 'applejack', 'makgeolli', 'merisa', 'stout', 'rak ', 'barley', 'obstwasser', 'tequilas', 'zivania', 'pito', 'rye', 'tuak', 'cashew', 'buckwheat', 'trester', 'sonti', 'vinjak', 'lozova a', 'borovi ka', 'akvavit', 'pinga', 'ouzo', 'absinthe', 'vodkas', 'rum', 'gin', 'parakari', 'wine', 'shochu', 'sahti', ' ljivovica', 'tsipouro', 'kirsch', 'madeira', 'millet', 'quinces', 'jabukova a', 'mamajuana', 'mbege', 'palinka', 'marc', 'clairin', 'brem', 'kvass', 'beer', 'cider', 'ogogoro', 'moonshine', 'witbier', 'kajsijeva a', 'maotai', 'choujiu', 'grappa', 'pastis', 'cauim', 'chungju', 'poir ', 'awamori', 'beers', 'blaand', 'majmunova a', 'highball', 'pulque', 'wines', 'ethanol', 'metaxa', 'mezcal', 'viljamovka', 'cocktails', 'kumis', 'singani', 'fermenting', 'kilju', 'gouqi', 'port', 'spirits', 'himbeergeist', 'nihamanchi', 'kasiri', 'whisky', 'porter', 'tej', 'vinsanto', 'mead', 'jenever', 'schwarzbier', 'vermouth', 'arrack', 'raki', 'basi', 'slivovitz', 'kefir', 'sangria', 'chicha', 'liqueurs', 'barleywine', 'calvados', 'sambuca', 'champagne', 'raicilla', 'poit n', 'sherry', 'baga o', 'p linka', 'liqueur', 'liquor', 'triple sec', 'bitters', 'rumchata', 'amaretto', 'irish cream', 'schnapps', 'grain alcohol']
garnish = ['olive', 'cucumber', 'peppermint', 'choco', 'chocolate', 'tobasco', 'syrup', 'wedge', 'whipped cream', 'caramel', 'vanilla extract', 'wedges', 'nutmeg', 'pepper', 'celery', 'salt', 'cinnamon', 'vanilla', 'ice', 'sugar', 'sugarcane']
fruits = ['cranberry', 'coconut', 'mango', 'limes', 'cherry', 'lime', 'pineapple', 'melon', 'watermelon', 'pear', 'strawberry', 'lemon', 'apple', 'gava', 'orange', 'banana', 'grape', 'pinapples', 'grapes', 'grapefruit', 'pomegranate']
nonAlcs = ['sprite', 'coke', 'coca', 'cola', 'soda', 'sparkling', 'ginger ale', 'milk', 'coffee']
juice = ['cranberry juice', 'coconut juice', 'mango juice', 'limes juice', 'cherry juice', 'lime juice', 'pineapple juice', 'melon juice', 'watermelon juice', 'pear juice', 'strawberry juice', 'lemon juice', 'apple juice', 'gava juice', 'orange juice', 'banana juice', 'grape juice', 'pinapples juice', 'grapes juice', 'grapefruit juice', 'pomegranate juice']

X = []
Y = []
with open('results.txt') as f:
    for line in f:
        if(ast.literal_eval(line)[1] != 0.0):
            X.append(ast.literal_eval(line)[0])
            Y.append(ast.literal_eval(line)[1])

# one hot encoding
a = np.zeros((len(X), len(alcohol) + len(garnish) + len(fruits) + len(nonAlcs) + len(juice)))
for row in range(len(X)):
    for i in range(4):
        a[row][X[row][i]] = 1
        a[row][len(alcohol) + X[row][i+4]] = 1
        a[row][len(alcohol) + len(garnish) + X[row][i+8]] = 1
        a[row][len(alcohol) + len(garnish) + len(fruits) + X[row][i+12]] = 1
        a[row][len(alcohol) + len(garnish) + len(fruits) + len(nonAlcs) + X[row][i+16]] = 1

model = Sequential()
#model.add(Dense(12, input_shape=(20, ), init='uniform', activation='sigmoid'))
#model.add(Dense(50, input_dim=len(alcohol) + len(garnish) + len(fruits) + len(nonAlcs) + len(juice), activation='relu', kernel_initializer='uniform'))
#model.add(Dense(50, activation='relu', kernel_initializer='uniform'))
#model.add(Dense(50, activation='relu', kernel_initializer='uniform'))
model.add(Dense(50, input_dim=len(alcohol) + len(garnish) + len(fruits) + len(nonAlcs) + len(juice), activation='selu', kernel_initializer='lecun_normal'))
model.add(Dense(50, activation='selu', kernel_initializer='lecun_normal'))
model.add(Dense(50, activation='selu', kernel_initializer='lecun_normal'))
model.add(Dense(50, activation='selu', kernel_initializer='lecun_normal'))
model.add(Dense(50, activation='selu', kernel_initializer='lecun_normal'))
model.add(Dense(50, activation='selu', kernel_initializer='lecun_normal'))
model.add(Dense(1, activation='relu', kernel_initializer='lecun_normal'))
model.summary()

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(a, np.array(Y), epochs=100, batch_size=50,  verbose=1, validation_split=0.3)

model.save('motherModel.h5')