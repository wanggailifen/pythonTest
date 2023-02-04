# 元组可以看做是不可以修改的list
testTuple = (1, 2, 3)
print(testTuple)
print(type(testTuple))

# 定义单个元素的元组一定要在后面加一个逗号,否则不是元组类型
testTuple2 = (1)
print("testTuple2 ", type(testTuple2))
testTuple3 = (1,)
print("testTuple3 ", type(testTuple3))

# 元素不可修改
testTuple[0] = 2
