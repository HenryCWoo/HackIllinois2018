import ast
from sklearn import svm
import numpy as numpy
from sklearn.externals import joblib

with open('result.txt') as f:


clf = svm.SVR()
clf.fit(features, result)
