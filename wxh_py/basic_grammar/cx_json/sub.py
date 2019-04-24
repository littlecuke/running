import re

s = 'JavaC#PyhtonPHPC#'

r = re.sub('C#','Go',s)
print(r)
r1 = re.sub('C#','Go',s,1)
print(r1)

s1 = s.replace('C#','Go')
print(s1)

def convert(value):
    pass

def convert1(value):
    matched = value.group()
    return '--'+matched+'--'


s1 = 'DHAKJ371DAS8D'
def convert2(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

s2 = re.sub('C#',convert,s)
print(s2)
s3 = re.sub('C#',convert1,s)
print(s3)
s4 = re.sub('\d',convert2,s1)
print(s4)

