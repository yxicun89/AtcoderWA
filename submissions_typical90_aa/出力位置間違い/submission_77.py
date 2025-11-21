n = int(input())
names = []
for _ in range(n):
    s = input()
    if not s in names:
        names.append(s)
        print(s)