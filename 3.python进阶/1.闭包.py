"""
什么是闭包?
定义双层嵌套函数，内层函数可以访问外层函数的变量
将内存函数作为外层函数的返回，此内层函数就是闭包函数
"""

# def outer(logo):
#     def inner(msg):
#         nonlocal logo
#         print(f"<{logo}>{msg}<{logo}>")
#         logo ="111"
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# fn1 = outer("outparam")
# fn1("大家好")
# fn1("你好呀")

def outer(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner


param = 0
print(f"param = {param}")
fn = outer(param)
fn(10)
fn(10)
fn(10)
fn(10)
print(f"param = {param}")
fn2 = outer(param)
fn2(10)
fn2(10)
print(f"param = {param}")
fn(10)
