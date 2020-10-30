
#simple function
def sum(a,b):
    c = a + b
    print(c)
sum(2,3)


#multiple argument pass
def sum1(*a):
    s = 0
    print(type(a))#each element of a is a tuple
    for i in a:
        s = s + i
    print(s)

sum1(1,5,7,23,45,100,4532,874,124)


#this function will return the square summation
def test(**b):
    s2 = []
    for i in b:
        print(i)
        summation = 0
        for j in b[i]:
            j = j**2
            summation+=j
            print(j)
        print(summation)
        s2.append(summation)
    return s2


temp = test(even_num=[2,4,6,8,10],odd_num=[1,3,5,7,9],prime=[2,3,5,7,11,13,17,19,23,29])
print(temp)


#recursion to find factorial
def recursion(n):
    s = 1
    if n > 0:
        s = n * recursion(n-1)
    else:
        s = 1
    print(n , "factorial :",s)
    return s

recursion(20)

