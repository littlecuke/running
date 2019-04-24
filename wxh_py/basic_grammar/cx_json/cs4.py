import re

a = 'pythonpythonpythonpythonpythonpython'


r = re.findall('(python){3}',a)
print(r)
# [] 或
# () 且
r1 = re.findall('(python){3}(JS)',a)
print(r1)


# re.I  使匹配对大小写不敏感
# re.L  做本地化识别（locale-aware）匹配
# re.M  多行匹配，影响 ^ 和 $
# re.S  使 . 匹配包括换行在内的所有字符
# re.U  根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X  该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
a1 = 'PythonC#JavaPHP'
r2 = re.findall('c#',a)
print(r2)
r3 = re.findall('c#',a1,re.I)
print(r3)

a2 = 'PythonC#\nJavaPHP'
r4 = re.findall('c#',a2,re.I)
print(r4)
r5 = re.findall('c#.{1}',a2,re.I|re.S)
print(r5)


