class Person: # 비공개 속성 => 클래스 외부에서 접근이 불가, 클래스 내부에서만 사용가능 => private attribute
    def __init__(self, name, age, weight):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        # self.weight = weight
        self.__weight = weight # 변수 앞에 `__`를 붙혀서 비공개 속성으로 변경

Jin = Person("진", 22, 72)        
print(Jin.name)
print(Jin.age)
print(Jin.weight)