import numpy as np

N = int(input())
List1 = []
List2 = []
for i in range(N):
    total = list(map(int, input().split()))
    List1.append(total)

for i in range(N):
    total = list(map(int, input().split()))
    List2.append(total)

arr1 = np.array(List1)
arr2 = np.array(List2)

output = arr1.dot(arr2)
print(output)



