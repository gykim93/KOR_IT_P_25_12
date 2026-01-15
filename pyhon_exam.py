# 지역변수
# 함수 내에서 정의된 변수
# 함수 내에서만 사용 가능

# 전역변수
# 함수 안이나 밖에서 어디서든 사용 가능

# global 있다면 => 함수 안과 바깥쪽이 동일
# global 없다면 => 함수 안과 밖은 서로가 남남

a = 20

def abc():
    global a
    a = 10
    print(a)
    
print(a)
abc()
print(a)