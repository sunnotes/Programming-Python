'''
Created on 2014年3月31日

@author: EASON
'''


'''
re.search() re.match() re.sub() re.findall()
'''


import re
m = re.search('[0-9]','abcd4ef')
print(m.group(0))


m = re.search("output_(\d{4})", "output_1986.txt")
print(m.group(1))


m = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
print(m.group("year"))