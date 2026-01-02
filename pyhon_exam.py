# 구구단 8단 제작과정
print("== v1 ==")
print("8 * 1 = 8")
print("8 * 2 = 16")
print("8 * 3 = 24")


print("== v2 ==")
print(f"{8} * {1} = {8}")
print(f"{8} * {2} = {16}")
print(f"{8} * {3} = {24}")

print("== v3 ==")
dan = 8
print(f"{dan} * {1} = {dan * 1}")
print(f"{dan} * {2} = {dan * 2}")
print(f"{dan} * {3} = {dan * 3}")

print("== v4 ==")
dan = 8
i = 1
print(f"{dan} * {i} = {dan * i}")
i = i + 1
print(f"{dan} * {i} = {dan * i}")
i += 1
print(f"{dan} * {i} = {dan * i}")

print("== v5 ==")
dan = 8
i = 1
if i <= 3:
    print(f"{dan} * {i} = {dan * i}")
    i += 1
if i <= 3:
    print(f"{dan} * {i} = {dan * i}")
    i += 1
if i <= 3:
    print(f"{dan} * {i} = {dan * i}")
    i += 1
if i <= 3:
    print(f"{dan} * {i} = {dan * i}")
    i += 1
    
# 빈복문 시작
# while 문
# 1 ~ 3 까지 출력
# 초기값
# 종료조건
# 보폭
i = 1 #초기값
while i <= 3: # 종료조건
  print(i)
  i += 1 #보폭 i = i + 1
          