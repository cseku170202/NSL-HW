import numpy as np

N, M = map(int, input().split())

List = []
for i in range(N):
    total = list(map(int, input().split()))
    List.append(total)

arr = np.array(List)
a = np.sum(arr, axis = 0)
b = np.prod(a)
print(b)


