# 捕获特定异常
try:
    1 / 0
except (NameError, ZeroDivisionError) as e:
    print(e)

print("------------------")
# 捕获所有异常
try:
    1 / 0
except Exception as e:
    print(e)
else:
    print("这是没有出现异常的时候需要做的事")
finally:
    print("这是无论是否出现异常都要做的事")

print("--------------------------")
# 异常的传递
def func01():
    numbers = 1 / 0


def func02():
    func01()


def main():
    try:
        func02()
    except Exception as e:
        print(f"这是main方法捕获的异常e = {e}")


main()
