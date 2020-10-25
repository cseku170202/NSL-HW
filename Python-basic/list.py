
List = [12,45,12,13,56,12,895,13,12,45,42]

for i in List:
    print(i)


print('\n')
print(List[-1])#access the last element of list

print(List[2:5])#access 2,3,4 index of List

print(List[2:])#access 2 to last index of List

print(List[:7])#access 0 to 6 index of List

print(List[5])

print(List[-5:-1])#access -5,-4,-3,-2 index of List

#length of list
print(len(List))

#add a new value at the end of List
List.append(123)
print(List)

#insert 1000 to index 2
List.insert(2,1000)
print(List)

#delete the last element
List.pop()
print(List)

#remove the first 13 from List
List.remove(13)
print(List)

#delete the item of 0 index
del List[0]
print(List)

#copy List to List1
List1 = List.copy()
print(List1)

#determine max and min
Max = max(List)
Min = min(List)
print(Max,Min)

#count the total appearance of 12 in List
c = List.count(12)
print(c)

#first index of 13 in List
ind = List.index(13)
print(ind)

#sort List
List2 = List.sort()
print(List)





