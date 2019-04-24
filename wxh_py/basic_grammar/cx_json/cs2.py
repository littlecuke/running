import re

s = "abc,acc,adc,aec,afc,ahc"

r = re.findall('a[cf]c',s)
print(r)
r1 = re.findall('[cf]',s)
print(r)
r2 = re.findall('[ad]c',s)
print(r2)
r3 = re.findall('a[c-f]c',s)
print(r3)

s2 = "python 1231&java\n890\r09"

r4 = re.findall('\w',s2)
print(r4)
r5 = re.findall('\W',s2)
print(r5)
r6 = re.findall('\s',s2)
print(r6)
r7 = re.findall('[a-z]',s2)
print(r7)
r8 = re.findall('[a-z][a-z][a-z]',s2)
print(r8)
r9 = re.findall('[a-z]{3,6}',s2)
print(r9)
