import numpy as np

N, M, P = input().split()
N = int(N)
M = int(M)
P = int(P)
check = 0

List1 = []
List2 = []

iteration = N + M

for i in range(iteration):
    check += 1
    total = input().split()
    length = len(total)
    if check <= N:
        List1.append(total)
    else:
        List2.append(total)

arr1 = np.array(List1, dtype='i')
arr2 = np.array(List2, dtype='i')

arr = np.concatenate((arr1, arr2), axis=0)
print(arr)



