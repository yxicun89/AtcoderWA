N = int(input())

S = [list(map(str, input().split())) for _ in range(N)]
re = []
ans = []
for i in range(N):
    if not S[i] in re:
        print(i)
