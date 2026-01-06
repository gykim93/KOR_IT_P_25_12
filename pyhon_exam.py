# 문제 : 입력받은 정수가 짝수인지 아닌지 판별해주는 함수 구현
def is_even(num):
    return num % 2 == 0
print(f"10은(는) 짝수인가요? : {is_even(10)}\n")
print(f"11은(는) 짝수인가요? : {is_even(11)}\n")
print(f"25은(는) 짝수인가요? : {is_even(25)}\n")
print(f"15은(는) 짝수인가요? : {is_even(15)}\n")