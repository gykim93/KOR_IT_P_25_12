# 리스트, 튜플, 세트, 딕셔너리
# 리스트 list
# 선언 : list1 = []
# 순서보장 : O
# 중복허용 : O
# 접근 : list1[idx]
# 수정 : O
# 추가 : append(), insert(), extend()
# 삭제 : remove(), pop(), clear()

# 튜플 tuple
# 선언 : t = ()
# 순서보장 : O
# 중복허용 : O
# 접근 : t[idx]
# 수정 : X
# 추가 : X
# 삭제 : X

# 세트 set
# 선언 : s = {}
# 순서보장 : X
# 중복허용 : X
# 접근 : X
# 수정 : X
# 추가 : add(), update()
# 삭제 : remove(), clear(), disacrd()

# 딕셔너리
# 선언 : dict = {key : value}
# 순서보장 : O
# 중복허용 : X(key)
# 접근 : dict[dict], dict.get(key)
# 수정 : O(value)
# 추가 : dict[key] = value, update()
# 삭제 : pop(), popitem(), clear

# 언제 써야되나?

# 여러 값들을 순서대로 관리 해야한다 ? => 리스트
# 한번 만들고나면 바뀔일이 없거나, 프로그램 실행 중에 실수라도 값이 바뀔 수 없는 그런상황을 막아야한다? 튜플
# 값의 존재여부가 중요하거나, 중복이 안된다면? => 세트
# key, value 통해서 효율적으로 데이터를 관리해야한다 => 딕셔너리

# 튜플
# 추가, 수정, 삭제 => 모두 불가능한 읽기전용
# => 수정하는 방법이 존재한다.
# tuple(), list()로 감싸면 된다.
print("튜플 => 리스트, 리스트 => 튜플")
t = ("귤", "사과")
print(t)
list1 = list(t) # 이렇게하면 리스트 형태로 바뀐다.
list1.append("포도") # 리스트에서 제공하는 append() 함수로 값을 추가.
print(list1)
t = tuple(list1)
print(t)

# 리스트
# 중복된 값이 허용된다. 만약에 어떤 상황에서 중복값들을 제거해야 할 때가 있다.
print("리스트 => 세트, 세트 => 리스트")
m_list = ["귤", "사과", "배", "배", "배"] # 과일 상자 => 배는 총 3개
print(m_list)
m_set = set(m_list) # set()로 바꿀 수가 있다.
print(m_set)
m_list = list(m_set)
print(m_list)

# 딕셔너리 : 순서보장O, 중복X(key)
print("리스트 => 딕셔너리, 딕셔너리 => 리스트")
m_list2 = ["귤", "사과", "배", "배", "배"]
print(m_list2)
m_dict = dict.fromkeys(m_list2)
print(m_dict)
m_list2 = list(m_dict)
print(m_list2)