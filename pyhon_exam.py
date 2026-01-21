# numpy
# import numpy as np

# 인덱싱

# li = [1, 2, 3, 4]
# print(li[1])
# print(li[0:2])

# 1차원 배열의 인덱싱
# arr1 = np.array([1, 2, 3, 4])
# print(arr1[0])  # 한개접근
# print("1차원 배열 인덱싱")
# # arr1[시작 : 끝 : 보폭]
# print(arr1[0:3:2])
# print(arr1[0::])
# print(arr1[:2:])

# 2차원 배열 인덱싱
# arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr2)
# [[1 2 3 4]
#  [5 6 7 8]]
# print(arr2[0,1])
# print(arr2[1,1])
# print(arr2[::, ::])
# print(arr2[0:2:, 1:3:])

# fancy 인덱싱 => 원하는 인덱스를 배열로 넘겨준다
# arr1 = np.array([10, 20, 30, 40, 50])
# # print(arr1)
# # print(arr1[[0, 1, 3]])

# arr2 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
# # print(arr2)
# print(arr2[[0, 1], [1, 3]])

# 논리값 인덱싱
# arr1 = np.array([1, 2, 3, 4])
# arr1[[True, False, True, False]]
# # print(arr1)
# # print(arr1[[True, False, True, False]])
# arr4 = arr1 > 2
# print(arr4)