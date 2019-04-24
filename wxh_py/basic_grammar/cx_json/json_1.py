import json

json_str = '{"name":"qiyue","age":18}'
#  json object => dict
stu = json.loads(json_str)
print(type(stu))
print(stu)
print(stu['name'])
print(stu['age'])

# json array
json_str_arr = '[{"name":"qiyue","age":18,"falg":false},{"name":"onenine","age":16}]'

stu_arr = json.loads(json_str_arr)
print(type(stu_arr))
print(stu_arr)