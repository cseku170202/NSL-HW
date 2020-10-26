
dictionary = {"Bangla":50, "English":66, "Math":80}
print(dictionary)

#access item from dictionary
x = (dictionary["Bangla"])
print(x)

x = dictionary.get("Math")
print(x)

#update an element in dictionary
dictionary["Math"] = 100
print(dictionary)

#access all the keys
for i in dictionary:
    print(i)

#access all the values
for i in dictionary:
    print(dictionary[i])
print('\n')

for i in dictionary.values():
    print(i)
print('\n')

for i in dictionary.items():
    print(i)#each i is a tuple
print('\n')

#add an element in dictionary
dictionary["ICT"] = 85
print(dictionary)

#delete the element with key "English"
dict = dictionary.pop("English")
print(dict)
print(dictionary)

#delete the last inserted element in the distinary
d = dictionary.popitem()
print(d)#d is a tuple here
print(dictionary)

dictionary["English"] = 78
dictionary["Physics"] = 82
print(dictionary)

del dictionary["Math"]
print(dictionary)

dictionary1 = dictionary.copy()
print(dictionary1)

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_list = [i for i in list if i%2!=0]
print(odd_list)

sentence = "I am shymun"
vowels = "aeiou"
filter = []
for i in sentence:
    if i not in vowels:
        filter.append(i)

print(''.join(filter))

#list comprehension
sentence1 = "I am shymun Islam"
vowels1 = "aeiouAEIOU"
filter1 = [i for i in sentence1 if i not in vowels1]
print(''.join(filter1))




