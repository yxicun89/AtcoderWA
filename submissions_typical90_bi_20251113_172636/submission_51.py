Q = int(input())
tops = []
bottoms = []
tp, btm = 0, 0
ans = []
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        tops.append(x)
        tp += 1
    elif t == 2:
        bottoms.append(x)
        btm += 1
    elif x > tp:
        ans.append(bottoms[x - tp - 1])
    else:
        ans.append(tops[tp - x])

print(ans)