import re

n = input()
n = int(n)
List = []
in_css_file = False
pattern = r"#[a-f A-F 0-9]{3,6}"

for i in range(n):
    line = input()
    if '{' in line:
        in_css_file = True
    elif '}' in line:
        in_css_file = False
    elif in_css_file:
        for instance in re.findall(pattern, line):
            print(instance)




