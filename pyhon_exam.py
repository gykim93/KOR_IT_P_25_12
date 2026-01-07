# 소수판별기
def is_prime_number(num):
    if num == 1:
        return False
    i = 2
    while i < num : # 2부터 num 까지의 수 중에서 num을 나눠 떨어지면 소수가x
        if num % i == 0:
            return False
        i += 1
    return True # 위 조건과 반복문을 모두 만족하지 않았다면 소수다.

#문제 : 입력받은 숫자가 10이라고 할때 1부터 10 사이에 존재하는 모든 소수를 출력하는 함수 구현

def print_1_to_n_prime_numbers(num):
    i = 1
    while i <= num:
        if is_prime_number(i):
            print(i)
        i += 1

print_1_to_n_prime_numbers(10)