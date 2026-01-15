# 상속 => 물려받다, 물려받은 기능을 유치한채 다른 기능을 추가
# 물려주는 클래스 => 부모클래스
# 물려받는 클래스 => 자식클래스


# 부모클래스
class Person():
    def hi(self):
        print("하이")

    def hello(self):
        print("헬로")


# 자식클래스 => 자식클래스의 메서드(함수) 갯수는 부모클래스보다 같거나 많다.
class Student(Person):
    def study(self):
        print("공부")

    def hello(self): # 메서드 오버라이딩
        print("안녕~~")

    def hello2(self):
        super().hello()
    # hello2 함수에 super().hello() 호출하게 되면 부모클래스의 hello 메서드가 호출이 된다.
    # Student 클래스 => 만들어진 객체는 2개의 hello 메서드를 현재 가지고 있는 상태.

Jin = Student()
Jin.hi()
Jin.hello()
Jin.study()
Jin.hello2()

print("=======")
Paul = Person()
Paul.hi()
Paul.hello()
Paul.study()