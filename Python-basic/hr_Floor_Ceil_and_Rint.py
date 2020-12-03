import numpy as np

total = input().split()
length = len(total)
List = []

for i in total:
    i = float(i)
    List.append(i)

arr = np.array(List)
np.set_printoptions(sign=" ")
a = np.floor(arr)
b = np.ceil(arr)
c = np.rint(arr)
print(a)
print(b)
print(c)



