# 装饰器就是使用创建一个闭包函数，在闭包函数内调用目标函数
# 可以达到不改动目标函数的同时，增加额外的功能。
def outer(func):
    def inner():
        print("我要起床了")
        func()
        print("我起来了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中。。。")
    time.sleep(random.randint(1, 3))


sleep()
