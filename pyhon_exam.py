# 문제 - for문으로 1부터 100까지 출력
# for i in range(1, 101):
#     print(i)
# 문제 - for문으로 100부터 1까지 출력
# for i in range(100, 0, -1):
#     print(i)
# 문제 - for문으로 1부터 100 사이의 짝수만 출력
# for i in range(2, 101, 2):
#     print(i)
# 문제 - for문으로 100부터 1 사이의 짝수만 출력
# for i in range(100, 0, -2):
#     print(i)
# 문제 - for문으로 구구단 8단 출력
# dan = 8
# for i in range(1, 10):
#     print(f"{dan} * {i} = {dan * i}")
# 문제 - for문으로 구구단 1단 ~ 9단 출력
# for dan in range(1, 10):
#     print(f"=={dan}단==")
#     for i in range(1, 10):
#         print(f"{dan} * {i} = {dan * i}")
# 문제 : for문으로 1부터 n사이에 존재하는 소수의 합을 반환하는 함수 구현
# def is_prime_number(num):
#     if num == 1:
#         return False
    
#     for i in range(2, num): # 2부터 num 까지의 수 중에서 num을 나눠 떨어지면 소수가x
#         if num % i == 0:
#             return False
        
#     return True # 위 조건과 반복문을 모두 만족하지 않았다면 소수다.

# def get_1_to_n_prime_sum(n):
#     s = 0
#     for i in range(1, n + 1):
#         if is_prime_number(i):
#             s += i
#     return s

# n = 10
# print(f"1부터 {n}사이에 존재하는 소수의 합 : {get_1_to_n_prime_sum(n)}")
# n = 100            
# print(f"1부터 {n}사이에 존재하는 소수의 합 : {get_1_to_n_prime_sum(n)}")

# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력
# a = [2, 1, 5, 6, 7]
# for i in a:
#     print(i)