
sum = 0
for i in range(0,10):
    sum+=i
    print(i)
print(sum)
print('\n\n')


for i in range(0,100,5):
    print(i)
print('\n\n')


for i in range(100,0,-5):
    print(i)
print('\n\n')



list = [12,67,23,56,134,876,13]
for x in list:
    print(x)
print('\n\n')


for x in list[2:5]:
    print(x)
print('\n\n')



for x in list[2:]:
    print(x)
print('\n\n')



for x in list[:5]:
    print(x)
print('\n\n')



for x in list[-5:-1]:
    print(x)
print('\n\n')



for x in list[:-1]:
    print(x)
print('\n\n')


string = "This is bangladesh"
for i in string:
    word = i.split()
    for character in word:
        print(character)




