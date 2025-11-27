n = int(input())

name_set = set()
ans = []
for i in range(n):
    s = input()
    if not s in name_set:
        name_set.add(s)
        ans.append(i)