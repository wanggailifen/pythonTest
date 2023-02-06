money = 50
a = 100
print("money = ", money)

# 类型转换
print(type(int("50")))

# 字符串格式化
name = "张三"
year = 1999
print("我的名字是%s,今年是%d年" % (name, year))
print(f"我的名字是{name},今年是{year}年")

# 控制台输入
# name = input("你是谁?")
# print(f"你是{name}")

if year > 2000:
    print("成立！")
else:
    print("不成立哦")
print("呵呵呵")

# while 循环
i = 1
while i <= 10:
    print(i)
    i = i + 1

# for循环
print("----for循环-----")
name = "abcdefg"
for x in name:
    print(x)

# range语句   start, end, step
print("----range语句-----")
rangeResult = range(1, 10, 2)
rangeResult = range(1, 10)
for x in rangeResult:
    print(x)

i = 0
for i in range(5):
    print(i)
print(i)



