# -*- coding: utf8 -*-
'''
Created on 2014年5月15日

@author: EASON
'''
import humansize

if __name__ == '__main__':
    username = 'mark'
    password = 'PapayaWhip'
    print("{0}'s password is {1}".format(username, password))
    

    si_suffixes = humansize.SUFFIXES[1000]      
    print(si_suffixes)
    print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))  
