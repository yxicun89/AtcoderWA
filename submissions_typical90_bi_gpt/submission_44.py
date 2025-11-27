n = int(input())
t = [list(map(int, input().split())) for i in range(n)]
a = []
for ts in t:
    if ts[0] == 1:
        a.append(ts[1])
    elif ts[0] == 2:
        a.insert(0, ts[1])
    else:
        print(a[ts[1] - 1])