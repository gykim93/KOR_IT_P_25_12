# 함수 => 자판기
# 매개변수 => 데이터 투입구
# 인자 => 동전(데이터)
# 리턴 => 데이터 배출구
# 함수 안에 return 한 개만 사용가능 단 아래와 같은 경우는 제외.
def plus(a, b):
    if a + b == 5:
        return a + b
    else:
        return 7
    
k = plus(3, 3)
print(k)