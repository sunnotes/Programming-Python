# -*- coding: utf8 -*-
'''
Created on 2014年5月15日

@author: EASON
'''
from fibonacci import fib


if __name__ == '__main__':
    for n in fib(1000):      
        print(n)
    
    list(fib(1000))