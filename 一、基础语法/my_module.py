def test(a, b):
    print(a + b)


# 模块内的方法再被import时会自动调用
print("这是模块内的方法")
test(1, 2)
print("---------------")

if __name__ == '__main__':
    test(1,2)
    print("__name__中的方法不会自动执行")
