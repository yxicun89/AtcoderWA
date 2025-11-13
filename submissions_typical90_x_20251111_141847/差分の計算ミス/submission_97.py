N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Ad = {}
Bd = {}

for v in A:
    if v in Ad:
        Ad[v] += 1
    else:
        Ad[v] = 1

for v in B:
    if v in Bd:
        Bd[v] += 1
    else:
        Bd[v] = 1
acnt = 0
bcnt = 0
for v in Ad:
    acnt += v*Ad[v]

for v in Bd:
    bcnt += v*Bd[v]

if (acnt - bcnt) > K:
    print('No')
    exit()

if (acnt - bcnt)%2 == 0:
    if K%2 == 0:
        print('Yes')
    else:
        print('No')
else:
    if K%2 == 0:
        print('No')
    else:
        print('yes')
    





