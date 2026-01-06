# 문제 : 5칙연산을 수행하는 함수를 만들어주세요.

# plus 함수 구현
def plus(a, b):
    return a + b

print(f"3 더하기 5는 {plus(3, 5)} 입니다.")
# 출력 => 3 더하기 5는 8 입니다.

# plus_3_nums 함수 구현
def plus_3_nums(a, b, c):
    return a + b + c
print(f"3 더하기 5 더하기 7은 {plus_3_nums(3, 5, 7)} 입니다.")
# 출력 => 3 더하기 5 더하기 7은 15 입니다.

# minus 함수 구현
def minus(a, b):
    return a - b
print(f"10 빼기 5 는 {minus(10, 5)} 입니다.")
# 출력 => 10 빼기 5 는 5 입니다.

# multiply 함수 구현
def multiply(a , b):
    return a * b
print(f"10 곱하기 5 는 {multiply(10, 5)} 입니다.")
# 출력 => 10 곱하기 5 는 50 입니다.

# mod 함수 구현
def mod(a, b):
    return a % b
print(f"4를 3으로 나눈 나머지는 {mod(4, 3)} 입니다.")
# 출력 => 4를 3으로 나눈 나머지는 1 입니다.

# div 함수 구현
def div(a, b):
    return a // b
print(f"4를 3으로 나눈 몫은 {div(4, 3)} 입니다.")
# 출력 => 4를 3으로 나눈 몫은 1 입니다.

# div2 함수 구현
def div2(a, b):
    return a / b
print(f"4를 3으로 나눈 결과는 {div2(4, 3)} 입니다.")
# 출력 => 4를 3으로 나눈 결과는 1.3333333333333333 입니다.