#  r 只读    w 覆盖    a 追加
# encoding是关键字传参，因为它不在第三位
file = open("test/123.txt", "r", encoding="UTF-8")
print(type(file))

# print(file.read(3))
# print(file.read(3))

# lines = file.readlines()
# print(lines)

for line in file:
    print(line)

file.close()

# with open 会在执行完语句块后自动close
with open("test/123.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(line)

# w模式 打开一个不存在的文件，会自动创建
# close调用的时候会内置flush功能
with open("test/1234.txt", "w") as file:
    file.write("这是新加的内容")
    # file.flush()


