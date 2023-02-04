# 字典的key不能是字典
my_dict = {
    "1": "哈哈",
    "2": "呵呵"
}
print(my_dict.get("1"))
print(my_dict["1"])

print(my_dict.keys())

print(my_dict.values())


my_dict.pop("2")
print(my_dict)