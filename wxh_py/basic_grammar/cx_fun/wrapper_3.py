import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print("this funtion named :" + func_name)
@decorator
def f2(func_name,func_name2):
    print("this funtion named :" + func_name +" and " + func_name2)

@decorator
def f3(func_name,func_name2,**kw):
    print("this funtion named :" + func_name +" and " + func_name2)
    print(kw)

f1("name1")
f2("name1","name2")
f3("name1","name2",a=1,b=2,c="123")

def print_time():
    print(time.time())

