class Person():
    def __init__(self):
        print("Person __init__ 호출")
        self.hello = "안녕"

class Student(Person):
    def __init__(self):
        print("Student __init__ 호출")        
        super().__init__() # 부모의 생성자를 호출한다.
        self.classroom = "A class"

Jin = Student()        
print(Jin.classroom)
print(Jin.hello)

# 자식클래스에 __init__ 생성자가 있다면 super().__init__() 써줘야된다.(안써주게 되면 자동으로 호출x)
# 자식클래스에 __init__ 생성자가 없다면 super().__init__() 생략가능(자동으로 호출)

class Person2():
    def __init__(self):
        print("Person init 호출")
        self.hello = "안녕"
    def print_hi(self):
        print("안녕하세요")    

class Student2(Person2):
    pass
Jin2 = Student2()