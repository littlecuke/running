def add(x,y):
    return x+y

r = lambda x,y:x+y
print(add(1,2))
print(r(1,2))

x = 18
y = 17
age = x if x > y else y
print(age)

list_x = [1,2,3,4,5,6,7]
list_y = [1, 4, 9, 16, 25, 36, 49]
r1 = map(lambda x:x*x,list_x)
print(list(r1))
r2 = map(lambda x,y:x*x+y,list_x,list_y)
print(list(r2))