# 문제 - 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.(개념 : 함수, 반복문, 리턴)
# 소수 => 1과 자기자신 제외하고 나눠지지 않는 수

def is_prime_number(num):
    if num == 1:
        return False
    i = 2
    while i < num : # 2부터 num 까지의 수 중에서 num을 나눠 떨어지면 소수가x
        if num % i == 0:
            return False
        i += 1
    return True # 위 조건과 반복문을 모두 만족하지 않았다면 소수다.

print(f"1은 소수입니다 : {is_prime_number(1)}")        
print(f"3은 소수입니다 : {is_prime_number(3)}")
print(f"4는 소수입니다 : {is_prime_number(4)}")
print(f"5는 소수입니다 : {is_prime_number(5)}")
print(f"6는 소수입니다 : {is_prime_number(6)}")
print(f"7는 소수입니다 : {is_prime_number(7)}")
print(f"1000은 소수입니다 : {is_prime_number(1000)}")