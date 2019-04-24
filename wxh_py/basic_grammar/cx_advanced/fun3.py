
orign = 0
# orign 作为全局变量使用 global
#
def go(step):
    global orign
    new_step = orign + step
    orign = new_step
    return orign

print(go(2))
print(go(2))
print(go(2))

#  pos 会被理解为全局变量
#  nonlocal 应用
def factory(pos):
    def go(step):
        nonlocal pos
        new_step = pos + step
        pos = new_step
        return new_step
    return go
tourist = factory(orign)
print(tourist(3))
print(tourist(3))
print(tourist(3))
