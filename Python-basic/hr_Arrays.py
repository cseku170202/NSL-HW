import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    a = []
    for i in arr:
        i = float(i)
        a.append(i)
    a.reverse()
    b = numpy.array(a)
    return b


arr = input().strip().split(' ')
result = arrays(arr)
print(result)