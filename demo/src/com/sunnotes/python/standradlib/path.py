'''
Created on 2014年3月31日

@author: EASON
'''
#os.path包
#os.path包主要是处理路径字符串，比如说'/home/vamei/doc/file.txt'，提取出有用信息。

import os.path
path = '/home/vamei/doc/file.txt'

print(os.path.basename(path))    # 查询路径中包含的文件名
print(os.path.dirname(path))     # 查询路径中包含的目录

info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')  # 使用目录名和文件名构成一个路径字符串

p_list = [path, path2]
print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分



print('--------------')

import glob
print(glob.glob('/home/vamei/*'))