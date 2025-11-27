n = int(input())
s = set()
for i in range(n):
    S = input()
    if S in s:
        continue
    s.add(S)
    print(S)