import numpy as np

N = int(input())
List = []

for i in range(N):
    total = list(map(float, input().split()))
    List.append(total)

arr = np.array(List)
output = np.linalg.det(arr)
print(round(output, 2))





