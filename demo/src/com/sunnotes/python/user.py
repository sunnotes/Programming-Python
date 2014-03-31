#coding = utf8
'''
Created on 2014-03-31

@author: EASON
'''



a = [1,2,3]
print(hasattr(a,'append'))

print('------------')

a = [1, 2, 3]
print (a.__class__)
print (a.__class__.__name__)


print('------------')
print(list.__base__)


print('------------')
import sys
print(sys.path)

print('------------')
# define class
class Me(object):
    def test(self):
        print ("Hello!")

def new_test():
    print ("New Hello!")

me = Me()


hasattr(me, "test")               # 检查me对象是否有test属性

getattr(me, "test")               # 返回test属性

setattr(me, "test", new_test)     # 将test属性设置为new_test

delattr(me, "test")               # 删除test属性

isinstance(me, Me)                # me对象是否为Me类生成的对象 (一个instance)

issubclass(Me, object)            # Me类是否为object类的子类

print("I'm %s. I'm %d year old" % ('Vamei', 99))