import numpy as np

N, M = input().split()
N = int(N)
M = int(M)
List = []

for i in range(N):
    total = list(map(int, input().split()))
    List.append(total)

arr = np.array(List)
a = np.min(arr, axis = 1)
b = np.max(a)
print(b)



