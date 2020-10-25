
list = [1,2,56,89,23,55,45]

if 2 in list:
    print("yes")
else:
    print("no")


a = input("Enter a number : ")
a = int(a)
#simple if else for checking whether a number is even or odd
if a%2==0:
    print("Even Number")
else:
    print("Odd Number")



#simple program for if else
b = int(input("Enter marks in between 0 to 100 : "))
if b >= 80 and b <=100:
    print("A+")
elif b >=75 and b <=79:
    print("A")
elif b >=70 and b <=74:
    print("A-")
elif b >=65 and b <=69:
    print("B+")
elif b >=60 and b <=64:
    print("B")
elif b >=55 and b <=59:
    print("B-")
elif b >=50 and b <=54:
    print("c+")
elif b >=45 and b <=49:
    print("c")
elif b >=40 and b <=44:
    print("d")
else:
    print("F")




a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

#nested if else
if a > b:
    if b > c:
        print(a)
    else:
        if a > c:
            print(a)
        else:
            print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)



