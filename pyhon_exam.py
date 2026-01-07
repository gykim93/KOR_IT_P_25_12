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

# 문제 : 1부터 1000사이에 존재하는 소수들의 개수를 출력해주세요.

count = 0
i = 1
while i <= 1000:
    if is_prime_number(i):
        count += 1
    i += 1
    
print(f"1부터 1000사이에 존재하는 소수들의 개수 : {count}")