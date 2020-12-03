import numpy as np

N, M = map(int, input().split())
List = []
for i in range(N):
    total = list(map(int, input().split()))
    List.append(total)

arr = np.array(List)
print(np.transpose(arr))
print(arr.flatten())
