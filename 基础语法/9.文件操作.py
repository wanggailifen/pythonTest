#  r 只读    w 覆盖    a 追加
file = open("123.txt", "r", encoding="UTF-8")
print(type(file))

print(file.read(3))
print(file.read(3))
