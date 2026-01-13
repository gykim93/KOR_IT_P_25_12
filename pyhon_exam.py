# 전역데이터
command_list = [
    "add : 데이터 추가",
    "list : 데이터 조회",
    "update : 데이터 수정",
    "delete : 데이터삭제",
]

# 데이터 저장 리스트
list1 = []


# 함수
# help
def print_help():
    for comm in command_list:
        print(comm)


# add
def add_data():
    print("저장할 값을 입력해주세요 : ")
    a = input()
    list1.append(a)


# update
def update_data():
    print("몇번째 값을 수정하시겠습니까 : ")
    a = int(input())
    print("어떤 값으로 수정하시겠습니까? : ")
    b = input()
    list1[a - 1] = b


# delete
def delete_data():
    print("몇 번째 값을 삭제하시겠습니까? :")
    a = int(input())

    if a > len(list1):
        print("없는 데이터 입니다.")
    else:
        del list1[a - 1]
        print(f"{a}번째 값을 삭제 했습니다.")


# 메인 프로세스
while True:
    print("명령어를 입력해주세요 : ")
    comm = input()

    if comm == "exit":
        print("프로그램이 종료 되었습니다.")
        break
    elif comm == "help":
        print_help()
    elif comm == "add":
        add_data()
    elif comm == "list":
        print(list1)
    elif comm == "update":
        update_data()
    elif comm == "delete":
        delete_data()
