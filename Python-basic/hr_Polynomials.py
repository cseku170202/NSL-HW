import numpy as np

List = list(map(float, input().split()))
x = int(input())

arr = np.array(List)
output = np.polyval(arr, x)
print(output)



