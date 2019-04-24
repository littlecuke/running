import time



def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(func_name):
    print("this funtion named :" + func_name)
@decorator
def f2(func_name,func_name2):
    print("this funtion named :" + func_name +" and " + func_name2)

f1("name1")
f2("name1","name2")