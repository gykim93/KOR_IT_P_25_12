# 리스트 컴프리헨션
# 회사에서 납품하는 제품
# 반품대상
items = ["RED-01", "RED-02", "BLUE-01", "BLUE-02"]
r_items = []
# print(items)
# print(r_items)

# for r in items:
#     if r.startswith("BLUE"):
#         r_items.append(r)
# print(r_items)

# 리스트 내에서 어떤 해당하는 조건의 데이터만 뽑아내거나
# 값을 바꿔서 새로운 리스트를 만들 때 사용할 수 있다/
# 문법
# 표현식 for 변수 in 반복대상 if 조건
# 리스트 컴프리헨션을 사용해서 3보다 큰 숫자만 뽑아서, 새로운 리스틑 만들어라
# m_list = [1,2,3,4,5]
# new_list = [x for x in m_list if x > 3]
# print(new_list)

print("모든 모델명 뒤에 SC")
items_cr = [r + "_SC" for r in items]
print(items_cr)

print("모든 모델명을 소문자로 바꾼다.")
items_lower = [r.lower() for r in items]
print(items_lower)

print("모든 모델명 중에 02번 제품만 뽑느데 뒤에 (new)라는 문장을 붙힌다.")
items_new = [r + "_(new)" for r in items if r.endswith("02")]
print(items_new)
