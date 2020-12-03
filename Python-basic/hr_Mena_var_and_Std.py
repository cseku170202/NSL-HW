import numpy as np

N, M = map(int, input().split())
List = []
for i in range(N):
    total = list(map(int, input().split()))
    List.append(total)

arr = np.array(List)
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
aa = np.std(arr)
print(round(aa, 11))




