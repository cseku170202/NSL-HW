
string1 = "This is My country. "
string2 = "I want to do something for my country."
print(string1)
print(string2)
List = []

#merge two strings
result = string1 + string2
print("Merge strings :",result)


#extract each word from the string and save it to a list
print("Extract each word from the string: ")
s = result.split()
for i in s:
    List.append(i)
    print(i)

print(List)

s = result.split("country")
print(s)

s = result.lstrip("This ")
print(s)

s = result.rstrip("country.")
print(s)

if s.startswith("This"):
    print("The string starts with This")


if s.endswith("country."):
    print("The string ends with country.")
else:
    print("The string doesn\'t ends with country.")

upper = s.upper()
print(upper)

lower = s.lower()
print(lower)

b = "Bangladesh"
print(b)
d = b.replace("an","_MY_")
print(d)