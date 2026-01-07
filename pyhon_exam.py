# 나이 10살 20살 30살
# age = 10
# age = 20
# age = 30

ages = [] # 빈 리스트 객체를 하나 만들었다.
# 객체를 조종할 수 있는 리모콘 ages라는 변수에 들어간다.

ages2 = ages # ages 변수 안에 들어있는 리모콘이 복사되서 ages2 변수에 들어간다.

ages.append(10) 
ages.append(20)
ages.append(30)

ages3 = []

print(ages)

# 위 코드 객체는 2개
# append() 함수는 파이썬에서 리스트의 끝에 새로운 요소를 추가하는 메서드(함수)

# 리스트생성
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.append('orange')
print(fruits)

# 리스트 객체 안에 요소 접근 => 인덱스
print(fruits[0]) 
print(fruits[1])
print(fruits[2])
print(fruits[3])