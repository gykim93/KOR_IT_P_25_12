# 포함관계
# 자동차 클래스가 엔진 클래스의 인스턴스를 포함하는 것을 생각
# 자동차는 엔진 없이는 작동x, 자동차 클래스는 엔진 클래스의 인스턴스를 내부에 포함
# 포함관계에서는 클래스 간에 부모 자식이라는 개념X
# 대신에 한 클래스가 다른 클래스의 인스턴스를 포함하는 관계

class Person():
    def hi(self):
        print("안녕")

class Add_Person():
    def __init__(self):
        self.person_directiory = [] # 사람 인명부에 사람을 append 한다.
    
    def add_person(self, person):
        self.person_directiory.append(person)

# Person 객체 생성
person1 = Person()            
person2 = Person()

add_person_instance = Add_Person()

add_person_instance.add_person(person1)
add_person_instance.add_person(person2)

for person in add_person_instance.person_directiory:
    person.hi()