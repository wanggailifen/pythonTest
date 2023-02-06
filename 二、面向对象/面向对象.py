class Student:
    name = None
    age = None
    __sex = None

    def __private_method(self):
        print("hello,this is __private_method")

    def sayHello(self):
        self.__private_method()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sex = "男"

    def __str__(self):
        return f"[Student] name={self.name},age={self.age},sex={self.__sex}"

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other) -> bool:
        return (self.name == other.name) & (self.age == other.age)


# 继承
class JuniorStudent(Student):
    major_class = None

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.__sex = "男"
        self.major = major

    def print_major_class(self):
        print(f"我的主修课程是{self.major_class}")


student1 = Student("张三", 18)
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
