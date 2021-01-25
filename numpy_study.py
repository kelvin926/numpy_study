import numpy as np
print(np.__version__)

a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print(type(a1))
print(a1.shape)
print(a1[0], a1[1], a1[2], a1[3], a1[4])
a1[0] = 4
print(a1)

a2 = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
print(a2)
print(a2.shape)
print(a2[0, 0], a2[2, 2])

a3 = np.array([ [ [1,2,3], [4,5,6] ],
               [ [7, 8, 9], [10, 11, 12] ] ])
print(a3)
print(a3[0,0,1])
print(a3.shape)

a4 = np.zeros(10)
print(a4)

a5 = np.ones(10)
print(a5)

a6 = np.ones((3, 3))
print(a6)

a7 = np.full((3,3), 3.14)
print(a7)

a8 = np.eye(3) #단위 행렬
print(a8)

a9 = np.tri(3) #삼각 행렬
print(a9)

b1 = np.empty(10) #초기화 하지 않은 배열 생성 - 기존 메모리 위치에 존재하는 값이 있음.
print(b1)

b2 = np.zeros_like(a3) #shape따기
print(b2)

b3 = np.ones_like(a3) #shape따고 1 넣기
print(b3)

b4 = np.full_like(a3, 10) #shape따고 입력값 풀로.
print(b4)


