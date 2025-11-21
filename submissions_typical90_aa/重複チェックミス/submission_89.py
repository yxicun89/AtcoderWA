n = int(input())
cnt = []
d = {"-" : 0}
p = 0
for i in range(n):
    str = input()
    if str not in d:
        d[str] = {str: 1}
        cnt.append(i+1)
        p += 1

print(cnt)

