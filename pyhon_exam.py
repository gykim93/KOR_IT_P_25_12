# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력, len 사용
# a = [2, 1, 5, 6, 7]
# for i in range(len(a)):
#     print(a[i])
# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소들을 역순으로 출력, len 사용
# a = [2, 1, 5, 6, 7]
# for i in range(len(a) -1, -1, -1):
#     print(a[i])

# 문제 : 리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력
# end_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# current_month = 1
# for end_day in end_days:
#     print(f"{current_month}월은 {end_day}일까지")
#     current_month += 1
# 문제 : 리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력, len 사용
# end_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for i in range(len(end_days)):
#     print(f"{i + 1}월은 {end_days[i]}일까지")
# 문제 : 리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력, enumerate 사용
end_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# enumerate() 함수 => 리스트
for i, end_day in enumerate(end_days):
    month = i + 1 # month 변수에 인덱스 값에 1을 더해서 실제 월
    print(f"{month}월은 {end_day}일까지")