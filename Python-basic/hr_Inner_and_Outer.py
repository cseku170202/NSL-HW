import numpy as np

List1 = list(map(int, input().split()))
List2 = list(map(int, input().split()))

arr1 = np.array(List1)
arr2 = np.array(List2)

inner = np.inner(arr1, arr2)
outer = np.outer(arr1, arr2)

print(inner)
print(outer)



