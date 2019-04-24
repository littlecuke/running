import json
stu = [
    {'name':'qiyue','age':18,'falg':False},
    {'name':'onenine','age':16}
]

json_str = json.dumps(stu)
print(type(json_str))
print(json_str)