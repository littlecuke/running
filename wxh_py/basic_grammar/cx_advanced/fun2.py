# 闭包
# 函数 + 环境变量
# 不会受到外部数据干扰


# 注意：
# a 不能当做变量倍赋值
def f1():
    a = 10
    def f2():
        a = 25
        print("f2 : "+str(a))
    print("f1-1 : "+str(a))
    f2()
    print("f1 : "+str(a))

f1()
