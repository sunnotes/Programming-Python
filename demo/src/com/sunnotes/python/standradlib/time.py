'''
Created on 2014年3月31日

@author: EASON
'''
import time
print(time.time())   # wall clock time, unit: second
print(time.clock())  # processor clock time, unit: second


#time.sleep()可以将程序置于休眠状态，直到某时间间隔之后再唤醒程序，让程序继续运行。

print('start')
#time.sleep(10)     # sleep for 10 seconds
print('wake up')


st = time.gmtime()      # 返回struct_time格式的UTC时间
st = time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
s  = time.mktime(st)    # 将struct_time格式转换成wall clock time
print(s)



import datetime
t      = datetime.datetime(2012,9,3,21,30)
t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)