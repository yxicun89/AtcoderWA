# 重複チェックミス
N = int(input())

D = set()

S = [input() for i in range(N)]

for i,j in enumerate(S,1):

    if i in D:continue

    print(j)

    D.add(i)

