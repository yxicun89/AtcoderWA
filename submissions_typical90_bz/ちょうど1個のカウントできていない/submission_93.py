# -*- coding: utf-8 -*-

n, m = map(int, input().split())

ab = [list(map(int,list(input().split()))) for i in range(m)]

c = []

ban = []

for i in range(m):
    if ab[i][0] > ab[i][1]:
        if (ab[i][0] not in c) & (ab[i][0] not in ban):
            c.append(ab[i][0])
        elif ab[i][0] in c:
            ban.append(ab[i][0])
            c.remove(ab[i][0])
    elif ab[i][0] < ab[i][1]:
        if (ab[i][1] not in c) & (ab[i][1] not in ban):
            c.append(ab[i][1])
        elif ab[i][1] in c:
            ban.append(ab[i][0])
            c.remove(ab[i][1])

print(len(c))