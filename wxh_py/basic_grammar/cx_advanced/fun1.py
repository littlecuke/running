# 闭包
# 函数 + 环境变量
# 不会受到外部数据干扰

def curse_per():
    a= 10
    def curse(x):
        return a*x*x
    return curse

f = curse_per()
print(f)
print(f.__closure__)
print(f.__closure__[0].cell_contents)

print(f(2))
