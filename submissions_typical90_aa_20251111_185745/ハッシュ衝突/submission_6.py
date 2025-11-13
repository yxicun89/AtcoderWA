# ハッシュ値使ってるから衝突してエラー
# input

N = int(input())

S = [None] * (N)

for i in range(N):

    S[i] = input()



# logic

L = []



for i in range(N):

    cur = 0



    for j in range(len(S[i])):

        cur += (ord(S[i][j]) - ord('0')) * (100 ** (j)) % 1000000007



    L.append(cur)



D = {L[0]: 1}

F = [True]



for i in range(1, len(L)):

    if L[i] in D:

        F.append(False)

    else:

        F.append(True)

        D[L[i]] = 1



for i in range(len(F)):

    if F[i]:

        print(i+1)

