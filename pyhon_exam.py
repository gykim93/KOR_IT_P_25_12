print("== 인스턴스 메서드 ==")
# 인스턴스 메서드
class Person():
    def hi(self):
        print("hi")

Jin = Person()
Jin.hi()        

print("== 스태틱(정적) 메서드 ==")

# 정적 메서드 => 첫 번째 매개변수로 self는 필요없다.
class Calc():
    @staticmethod # 스태틱(정적) 메서드
    def add(a, b):
        print(a + b)

Calc.add(10, 20) # 클래스에서 바로 메서드(함수) 호출(실행)이 가능하다.

print("== 클래스 메서드 ==")

# 클래스 메서드
class Person2():
    count = 0 # 클래스 속성
    def __init__(self):
        Person2.count += 1
    
    @classmethod
    def print_count(cls): #클래스메서드
        print(f"사람이 총 {cls.count}명 있습니다.") # cls로 클래스 속성에 접근한다.

Person2.print_count()        
Jin2 = Person2()

Person2.print_count()  
Jin2 = Person2()      

Person2.print_count()  