
i = 0
while i < 6:
    print(i)
    i+=1
print('\n\n')


#simple while loop
List = [12,56,23,45,100,4,67,13]
n = len(List)

i = -1
sum = 0
while i < n:
    i+=1
    if i==2:
        continue
    if i==4:
        break
    print(List[i])
    sum+=List[i]

print("Summation :",sum)