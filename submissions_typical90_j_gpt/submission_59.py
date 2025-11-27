# input
N = int(input())
C = []
for i in range(N):
    C.append(list(map(int, input().split())))
Q = int(input())
L = []
for i in range(Q):
    L.append(list(map(int, input().split())))

# solve
class1 = []
class2 = []

# クラス分け
for i, s in enumerate(C):
    if s[0] == 1:
        class1.append([i+1, s[1]])
    else:
        class2.append([i+1, s[1]])

# 合計点数出力
for l in L:
    score1, score2 = 0, 0
    for c1, c2 in zip(class1, class2):
        if c1[0] > l[1]:
            break
        elif c1[0] >= l[0]:
            score1 += c1[1]
        if c2[0] > l[1]:
            break
        elif c2[0] >= l[0]:
            score2 += c2[1]
    print(f'{score1} {score2}')
