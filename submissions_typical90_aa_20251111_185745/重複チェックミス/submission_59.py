import re

n = int(input())
s = [input() for _ in range(n)]

set_li = []
set_str = ", ".join(set_li)

for i in range(n):
    pattern = re.compile(s[i])

    match = pattern.search(set_str)

    if match:
        continue
    else:
        print(i+1)
        set_li.append(s[i])
        set_li = list(set(set_li))
        set_str = ", ".join(set_li)