import numpy as np

List = []
a = input().split()

for i in a:
    i = int(i)
    List.append(i)
arr = np.array(List)
output = arr.reshape(3, 3)
print(output)