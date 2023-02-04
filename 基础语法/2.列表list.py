# list 列表  可以为不同数据类型  支持嵌套
testList = [1, 2, "A", True, [1, 2, 3]]
print(testList)
print(type(testList))

print(testList[0])
print(testList[4][2])
# -1 表示倒数第一个
print(testList[-1])

print(testList.index(2))
testList.insert(1, "haha")
print(f"插入元素后，结果为{testList}")

testList2 = [1, 2, 3]
testList.extend(testList2)
print(f"extend后，结果为{testList}")

# 删除元素
del (testList[0])
print(f"del后，结果为{testList}")
# 删除并返回被删除的元素
testList.pop(0)
print(f"pop后，结果为{testList}")
testList.remove(True)
print(f"remove后，结果为{testList}")

print(testList.count(2))
print(len(testList))
