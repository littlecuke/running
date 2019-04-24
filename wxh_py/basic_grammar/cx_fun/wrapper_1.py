import time
# 对修改是关闭的  对扩展是开放的
def f1():
    print("--1--")

def f2():
    print("--2--")


def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)

# 装饰器
# 大样
# def decorator():
#     def wrapper():
#         pass
#     return wrapper
# 实现
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


f = decorator(f1)
f()


@decorator
def f3():
    print("--3--")
f3()

def xpara(xpax):
    xpa1 =4
    def xpa(xpa1):
        return xpax+xpa1
    return xpa(xpa1)

print(xpara(3))
