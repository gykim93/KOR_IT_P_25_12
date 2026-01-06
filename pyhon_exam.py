# 매개변수 => 함수 외부에서 값을 가져온다.
# 함수 내부랑 외부를 연결해주는 매개체 그래서 매개변수
# 즉 a와 b를 연결하는 매개체
def print_dan(dan):
    print(f"== 구구단 {dan}단 출력 ==")
    i = 1
    while i <= 9:
        print(f"{dan} * {i} = {dan * i}")
        i += 1

print_dan(2)
# 위에 () 안쪽에 있는 숫자들을 보고 인자 또는 인수 또는 args(아규먼트)