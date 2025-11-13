N = int(input())

S = []
for i in range(N):
    S.append(input())

for j in range(N):
    if S[j] in S[:j]:
        print(j)