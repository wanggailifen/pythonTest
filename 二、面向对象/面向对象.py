from typing import Union

# 联合类型
my_list: list[Union[str, int]] = [1, 2, "haha"]
my_dict: dict[str, Union[str, int]] = {"name": "张三", "age": 18}


class Student:
    name: str = None
    age: int = None
    __sex = None  # type: str
    my_set = None  # type: set
    my_dict: dict[str, int] = {"a": 1}

    def __private_method(self):
        print("hello,this is __private_method")

    def sayHello(self):
        self.__private_method()

    def __init__(self, name: Union[str, int], age: int):
        self.name = name
        self.age = age
        self.__sex = "男"

    def __str__(self):
        return f"[Student] name={self.name},age={self.age},sex={self.__sex}"

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other) -> bool:
        return (self.name == other.name) & (self.age == other.age)


class People:
    address = None


# 继承   多继承优先级从左到右
class JuniorStudent(Student, People):
    major_class = None

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.__sex = "男"
        self.major = major

    def print_major_class(self) -> None:
        Student.sayHello(self)
        print(super().age)
        print(f"我的主修课程是{self.major_class}")


class JuniorStudent2(Student, People):
    pass  # 占位语句，仅仅为了保证完整性


student1: Student = Student("张三", 18)
print(student1)

student2 = Student("李四", 20)
print(student1.__lt__(student2))

student3 = Student("张三", 18)

print(student1.__eq__(student3))

student4 = Student("张三", 18)
print(student4)

student4.sayHello()

student5 = JuniorStudent("张三", 18, "数学")
student5.print_major_class()
print(student5)
