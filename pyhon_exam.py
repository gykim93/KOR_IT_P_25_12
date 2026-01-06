# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.
def print_dan(dan, limit): # 괄호 안쪽에 있는 dan, limit => 매개변수
    print(f"== {dan}단 ==")
    i = 1
    while i <= limit:
        print(f"{dan} * {i} = {dan * i}")
        i += 1
        
print_dan(1, 5) # 1단 * 5 => 1, 5 각각 1은 dan, 5 => limit
print_dan(2, 13) # 2단 * 13       