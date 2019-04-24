import re

s2 = "python 1231&java\n890\r09"
# 贪婪
r9 = re.findall('[a-z]{3,6}',s2)
print(r9)
# 非贪婪
res1 = re.findall('[a-z]{3,6}?',s2)
print(res1)


s3 = "pytho0python1pythonn2"
 # * 匹配0次或者无限多次
 # + 匹配1次或者无限多次
 # ? 匹配0次或者1次
res2 = re.findall('python*',s3)
print(res2)
res3 = re.findall('python+',s3)
print(res3)
res4 = re.findall('python?',s3)
print(res4)