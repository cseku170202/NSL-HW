import numpy as np

N, M = input().split()
N = int(N)
M = int(M)
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
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(arr1 // arr2)
print(np.mod(arr1, arr2))
print(np.power(arr1, arr2))


