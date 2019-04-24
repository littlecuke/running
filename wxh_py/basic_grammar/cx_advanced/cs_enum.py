from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)
#  代码实现
# 可变，没有防止相同值的功能
class TypeDiamond():
    yellow = 1
    green = 2

TypeDiamond.green = 3
print()
