# import time
# from time import sleep
from time import *
# import time as myTime

# 导入自定义模块
import my_module
from my_module2 import *

print("开始睡眠！")
# time.sleep(3)
sleep(1)
print("已经睡了1秒啦！")

# myTime.sleep(1)
# print("又睡了1秒啦！")


my_module.test(1, 3)

#  通过 from my_module2 import *  只能导入模块里面定义在__all__里面的变量
# test02(3, 2)
