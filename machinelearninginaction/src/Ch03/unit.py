'''
Created on Jan 31, 2014

@author: EASON
'''
import unittest

reload(trees.py)

class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    '''unittest.main()
    '''
    myDat,labels = trees.createDataSet() 
    print(myDat)
    