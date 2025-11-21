N = int(input())
score_1 = [0] * N
score_2 = [0] * N

for i in range(N):
    C, P = map(int, input().split())
    if i == 0:
        if C == 1:
            score_1[0] = P
            score_2[0] = 0
        elif C == 2:
            score_1[0] = 0
            score_2[0] = P
    elif i != 0:
        if C == 1:
            score_1[i] = score_1[i-1] + P
            score_2[i] = score_2[i-1]
        else:
            score_1[i] = score_1[i-1]
            score_2[i] = score_2[i-1] + P

#print(score_1, score_2)

Q = int(input())

for i in range(Q):
    L, R = map(int, input().split())
    L -= 2
    if L < 0:
        L = 0
    R -= 1
    if score_1[R] == score_1[L]:
        ans_1 = score_1[R]
    else:
        ans_1 = score_1[R] - score_1[L]

    if score_2[R] == score_2[L]:
        ans_2 = score_2[R]
    else:
        ans_2 = score_2[R] - score_2[L]
    print(ans_1, ans_2)

