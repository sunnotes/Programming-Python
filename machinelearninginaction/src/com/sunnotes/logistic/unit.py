'''
Created on 2014年4月2日

@author: EASON
'''


import logistic

dataArr,labelMat = logistic.loadDataSet()

weights = logistic.gradAscent(dataArr,labelMat)

print(weights)