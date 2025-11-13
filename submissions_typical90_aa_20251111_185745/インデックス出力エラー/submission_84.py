# 順序一致しない

n = int(input())

s = [input() for _ in range(n)]

dic = {key:value for value, key in enumerate(s)}

num = []

s.sort()

num.append(dic[s[0]] + 1)

for i in range(n - 1):

    if s[i] != s[i + 1]:

        num.append(dic[s[i + 1]] + 1)

num.sort()

for i in num:

    print(i)
