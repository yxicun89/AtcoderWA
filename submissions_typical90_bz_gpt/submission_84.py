N,M = map(int,input().split())
count_below = [0]*N

for i in range(M):
    a,b = map(int,input().split())
    if a > b:
        count_below[a-1] += 1
    else:
        count_below[b-1] += 1

ans = 0
for i in count_below:
    if i == 0:
        ans += 1

print(ans)