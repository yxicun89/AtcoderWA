q = int(input())
tz = [input().split() for i in range(q)]
res = []
ans = []
for i in range(q):
        if tz[i][0] == '1':
            res.insert(0,tz[i][1])

        elif tz[i][0] == '2':
            res.append(tz[i][1])

        elif tz[i][0] == '3':
            print(tz[i][1])