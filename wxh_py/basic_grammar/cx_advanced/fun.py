# 闭包

def curse_per():
    a= 25
    def curse(x):
        return a*x*x
    return curse

f = curse_per()
print(f)

print(f(2))