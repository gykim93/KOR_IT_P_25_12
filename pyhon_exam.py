# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.

def print8dan():
    dan = 8
    print("== 1번째 구구단 8단 출력 ==")
    i = 1
    while i <= 9:
        print(f"{dan} * {i} = {dan * i}")
        i += 1

print8dan()