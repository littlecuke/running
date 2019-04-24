import re

str = "473q389danGdfwna#￥……&SD……&……*……@@！……&@%@#￥@#……FSDGGWRQW#$@$"

res1 = re.findall("G",str);
print(res1)
print(res1.__len__())
res2 = re.findall("\d",str);
print(res2)
print(res2.__len__())
res3 = re.findall("\D",str);
print(res3)
print(res3.__len__())
