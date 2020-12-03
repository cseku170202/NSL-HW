import numpy as np

total = input().split()

List = []
for i in total:
    i = int(i)
    List.append(i)
a = tuple(List)

b = np.zeros((a), dtype='i')
c = np.ones((a), dtype='i')
print(b)
print(c)




