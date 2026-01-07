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

# 문제 : 1부터 n 사이의 수 중에서 소수의 개수 반환하는 함수 `get_1_to_n_prime_numbers_count` 를 구현해주세요.


# 1부터 n 사이의 수 중에서 소수의 개수 반환하는 함수
def get_1_to_n_prime_numbers_count(n):
  #여기서 구현해주세요.
    count = 0
    i = 1
    while i <= n:
        if is_prime_number(i):
            count += 1        
        i += 1
    return count

count = 0
number = 0

number = 1000
count = get_1_to_n_prime_numbers_count(number)
print(f"1부터 {number}사이에 존재하는 소수의 개수 : {count}개\n")
  # 출력 => 1부터 1000사이에 존재하는 소수의 개수 : 168개

number = 2000
count = get_1_to_n_prime_numbers_count(number)
print(f"1부터 {number}사이에 존재하는 소수의 개수 : {count}개\n")
  # 출력 => 1부터 2000사이에 존재하는 소수의 개수 : 303개
