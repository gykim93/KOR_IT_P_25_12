# 문제 : 입력받은 정수의 모든 약수를 출력하는 함수를 구현해주세요.
# 약수 => 나눴을 때 나머지가 0

def print_divisors(num):
  i = 1
  while i <= num:
      if num % i == 0:
          print(i)
      i += 1

print_divisors(1000)