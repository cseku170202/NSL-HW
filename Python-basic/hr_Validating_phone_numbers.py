import re

n = input()
n = int(n)
b = []
for i in range(n):
    a = input()
    a = str(a)
    b.append(a)
pattern = r"^(7|8|9)"
for i in b:
    single = str(i)
    l = len(single)
    if l == 10 and re.search(pattern, single) and single.isdigit():
        print("YES")
    else:
        print("NO")


