# numpy
import numpy as np

# ndArray ? N-dismensional Array의 약자, 다차원 배열
# ndArray 생성
# numpy.array([1,2,3,4])
# np.array([1,2,3,4])

# arr = [1,2,3,4] # 파이썬 리스트
arr1 = np.array([1, 2, 3, 4])  # 넘파이 ndArray

# print(type(arr))
# print(type(arr1))

# print(arr)
# print(arr1)

# 2차원 ndArray 생성
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# 3차원 ndArray 생성
arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])

# print(arr1)
# print("================")
# print(arr2)
# print("================")
# print(arr3)

# ndArray.ndim => 배열의 차원을 알 수 있다
# print("== ndArray.ndim ==")
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

# ndArray.shape => 모양
# print("== ndArray.shape ==")
# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)

# ndArray.size => 크기
# print("== ndArray.size ==")
# print(arr1.size)
# print(arr2.size)
# print(arr3.size)

# ndArray.dtype => 타입
# print("== ndArray.dtype ==")
# print(arr1.dtype)
# print(arr2.dtype)
# print(arr3.dtype)

""" arr1
[1 2 3 4]
================
arr2
[[1 2 3 4]
 [5 6 7 8]]
================
arr3
[[[1 2 3 4]
  [5 6 7 8]]

 [[1 2 3 4]
  [5 6 7 8]]] """
  
# 배열 생성 함수
# 0으로 채워진 행렬
# np.zeros((3,4)) 
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])
# 1로 채워진 행렬
# np.ones((2,3,4))
# array([[[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]],

#        [[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]]])
# # i로 채워진 행렬
# np.full((2,2), 5)
# array([[5, 5],
#        [5, 5]])

# like => 다른 배열의 모양을 본따서
# print(np.zeros_like(arr1))
# print("=======================")
# print(np.ones_like(arr2))
# print("=======================")
# print(np.full_like(arr3, 5))

# random => 난수
# np.random.seed(1) # 최초 난수생성 기준
# random_arr = np.random.randint(-100, 100, (2,3))
# # -100 ~ 100 사이에 있는 정수로 2 * 3 행렬 생성

# print(random_arr)
