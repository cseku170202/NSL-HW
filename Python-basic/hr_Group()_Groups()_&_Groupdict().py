import re

String = input()

pattern = r"([a-z A-Z 0-9])\1"
result = re.search(pattern, String)

if result:
    print(*result.groups())
else:
    print(-1)



