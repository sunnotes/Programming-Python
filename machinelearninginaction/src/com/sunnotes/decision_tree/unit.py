'''
Created on Jan 31, 2014

@author: EASON
'''
import unittest

from com.sunnotes.decision_tree import trees
#reload(trees.py)

class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    '''unittest.main()
    '''
    myDat,labels = trees.createDataSet() 
    print(myDat)
    
    print(trees.calcShannonEnt(myDat))
    
    myDat[0][-1] = 'maybe'
    print(myDat)
    
    print(trees.calcShannonEnt(myDat))
    
    myDat,labels = trees.createDataSet() 
    print(trees.calcShannonEnt(myDat))
    print(trees.chooseBestFeatureToSplit(myDat))
    print(myDat)