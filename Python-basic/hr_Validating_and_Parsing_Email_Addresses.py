import re

n = input()
n = int(n)

for i in range(n):
    single_input = input()
    name, email = single_input.split(" ")

    pattern = r"<[a-z][a-z A-Z 0-9\-\.\_]+@[a-z A-Z]+\.+[a-z A-Z]{1,3}>"
    if re.search(pattern, email):
        print(name + " " + email)


