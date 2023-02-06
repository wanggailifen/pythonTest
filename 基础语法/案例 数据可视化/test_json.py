import json




data = [
    {"name": "张三", "age": 11},
    {"name": "李四", "age": 12},
    {"name": "王五", "age": 13},
]

jsonstr = json.dumps(data, ensure_ascii=False)
print(jsonstr)


d = {"name": "张三", "age": 11}

jsonstr2 = json.dumps(d, ensure_ascii=False)
print(jsonstr2)

# 将字符串还原成json对象
str = '[{"name": "张三", "age": 11}, {"name": "李四", "age": 12}, {"name": "王五", "age": 13}]'
jsonObject = json.loads(str)
print(jsonObject)




