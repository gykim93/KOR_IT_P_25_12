# 문제 : 입력받은 정수가 3의 배수인지 알려주는 함수 구현
def is_3_multiple(num):
    return num % 3 == 0

print(f"10은(는) 3의 배수인가요? : {is_3_multiple(10)}\n")
print(f"12은(는) 3의 배수인가요? : {is_3_multiple(12)}\n") 





#문제 : 입력받은 정수가 100보다 큰지 알려주는 함수 구현
def is_bigger_than_100(num):
    return num > 100

print(f"128은(는) 100보다 큽니다. : {is_bigger_than_100(128)}\n")
print(f"28은(는) 100보다 큽니다. : {is_bigger_than_100(28)}\n")
print(f"100은(는) 100보다 큽니다. : {is_bigger_than_100(100)}\n") 


 # 문제 : 입력받은 정수의 모든 약수의 합을 리턴하는 함수를 구현해주세요.

def get_divisors_sum(num):
    s = 0
    i = 1
    while i <= num:
        if num % i == 0:
            s += i
        i += 1
    return s

s = get_divisors_sum(1000)

print(f"정수 1000의 약수의 합 : {s}")
# 출력 => 정수 1000의 약수의 합 : 2340 
 