# 函数
def test():
    print("hello")


# global 表示方法内的该局部变量是全局变量
num = 200


def test01():
    num = 500
    print(f"test01 num={num}")


def test02():
    global num
    num = 500
    print(f"test02 num={num}")


test01()
print(num)
test02()


# 函数与方法的区别
# 定义在类（class）里面的叫方法,其他无区别
class Test:
    def test03(self, num1, num2):
        return num1 + num2


myTest = Test()

result = myTest.test03(1, 3)
print(result)


# 函数多返回值
def test04():
    return 1, "haha", False


x, y, z = test04()
print(x)
print(y)
print(z)


# 关键字传参、默认值
def user_info(name, age, gender="女"):
    print(f"你的名字是{name}, 年龄是{age}, 性别是{gender}")


user_info(age=20, gender="男", name="小明")
user_info("小明", gender="男", age=20)
user_info("小明", age=20)


# 不定长参数  会以元组接收
def test05(*args):
    print(args)


test05("haha")
test05("haha", 123, False)


# 关键字传递的不定长 数据形式必须是 k-v对，会被字典接收
def test06(**kwargs):
    print(kwargs)


test06(name="张三", age=18, gender="男")


# 函数作为参数
def test_func(x, y, fun):
    result = fun(x, y)
    print(result)


def compute(x, y):
    return x + y


def compute2(x, y):
    return x * y


test_func(1, 3, compute)
test_func(1, 3, compute2)

# lambda
test_func(1, 3, lambda x, y: x + y)
