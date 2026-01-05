# 문제 - 구구단, 8단, 3단을 연달아 출력해주세요.
dan = 8
print(f"=={dan}단 ==")
i = 1
while i <= 9:
    print(f"{dan} * {i} = {dan * i}")
    i += 1

dan = 3
print(f"=={dan}단 ==")
i = 1
while i <= 9:
    print(f"{dan} * {i} = {dan * i}")
    i += 1
    
# 문제 - 1부터 5까지의 합을 출력해주세요.(개념 : while)
sum = 0

i = 1 # 초기값
while i <= 5: # 종료조건
    sum += i # 반복하면서 sum에 i값을 계속 넣어준다.
    i += 1 # 반복하는 동안에 i값은 1씩증가

print(f"1부터 5까지의 합 : {sum}")    