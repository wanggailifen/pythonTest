import json


class Student:

    name = None
    gender = None
    nationality = None
    native_place = None
    age = None


stu_1 = Student()
stu_1.name = "张三"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东"
stu_1.age = 22

# print(json.dumps(stu_1))