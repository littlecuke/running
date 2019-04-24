
from functools import reduce

list_x = [1,2,3,4,5,6,7]
list_y = [1,2,3,4,5]
list_z = ['1','2','3','4','5']
list_a = ['a','D','b','F','c']

r1 = map(lambda x,y:x*x,list_x,list_y)
print(list(r1))

# reduce 连续调用
r = reduce(lambda x,y:x+y,list_x)
print(r)
r2 = reduce(lambda x,y:x+y,list_z,'5')
print(r2)

# filter

def f(value):

    return value % 2 == 0
r3 = filter(f,list_x)
print(list(r3))