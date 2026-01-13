# 딕셔너리를 이용해서 회원 정보를 저장해주세요. 회원 정보는 아이디, 비밀번호, 이름으로 하겠습니다.
# 아이디가 hong123, 비밀번호가 1234, 이름이 홍길동인 회원
# 아이디가 sony7, 비밀번호가 7777, 이름이 손흥민인 회원
# 아이디가 ryu99, 비밀번호가 9999, 이름이 류현진인 회원
# 위 세명의 회원을 딕셔너리를 이용해 만들고 출력해주세요. 회원의 정보를 모두 출력해주세요.

"""
아이디 : hong123
비밀번호 : 1234
이름 : 홍길동
================
아이디 : sony7
비밀번호 : 7777
이름 : 손흥민
================
아이디 : ryu99
비밀번호 : 9999
이름 : 류현진
================
"""
user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}

user_list = [user1, user2, user3]
# 모든 회원 정보 출력
def print_all_users():
    for user in user_list:
        for key,value in user.items():
            print(f"{key} : {value}")
        print("================")
# print_all_users()
# # 모든 회원 아이디를 출력
# for user in user_list:
#     print(user["아이디"])

# hong123 아이디를 가진 회원의 이름 출력
# for user in user_list:
#     if user["아이디"] == "hong123":
#         print(user["이름"])

# hong123 아이디를 가진 회원의 비밀번호를 3333으로 수정 후 모든 회원 정보 출력
# for user in user_list:
#     if user["아이디"] == "hong123":
#         user["비밀번호"] = "3333"
# print_all_users()

# 아이디가 hong124, 이름 홍길순, 비밀번호 h1234 인 회원추가
user5 = {"아이디": "hong124", "비밀번호": "h1234", "이름": "홍길순"}
user_list.append(user5)
# print_all_users()

# 아이디가 중복될 시 추가 거부.
user5 = {}
user5["아이디"] = "hong123"
user5["비밀번호"] = "h1234"
user5["이름"] = "홍길"

flag = True
for user in user_list:
    if user["아이디"] == user5["아이디"]:
        flag = False
        print("이미 존재하는 아이디 입니다.")
        break
if flag:
    user_list.append(user5)    
    
print_all_users()    