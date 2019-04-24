import re

# re.match()
# re.search()

s = '5DHAKJ371DAS8D'

r = re.match('\d',s)
print(r.span())

r1 = re.search('\d',s)
print(r1.group())

s1 = 'life is short , i use python'
s2 = 'life is short , i use python , i love python'

r2 = re.search('life.*python',s1)
print(r2.group())
r3 = re.search('life(.*)python',s1)
print(r3.group(1))
r4 = re.search('life(.*)python(.*)',s2)
print(r4.group(2))
r5 = re.search('life(.*)python(.*)',s2)
print(r5.groups())