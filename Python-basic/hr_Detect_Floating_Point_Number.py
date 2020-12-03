import re

n = input()
n = int(n)
a = []
for i in range(n):
    b = list(input().split())
    a += b
pattern = r"^[+-]?[0-9]*\.[0-9]+$"
for i in a:
    i = str(i)
    if re.search(pattern, i):
        print("True")
    else:
        print("False")


