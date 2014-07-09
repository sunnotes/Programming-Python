'''
Created on 20140709

@author: EASON
'''
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
a.index(333)
a.remove(333)
a.reverse()
a.sort()
a.pop()
print(a)


##using lists as stack

stack = [3,4,5]
stack.append(6);
stack.append(7);

t = stack.pop();
print(t)
print(stack);

## using as queue



