N,M = map(int,input().split())
check = [1]*N
smaller = [0]*N

for _ in range(M):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    if check[a] == 0:
        continue
    if a > b:
        smaller[a] += 1
        if smaller[a] > 1:
            check[a] = 0
    else:
        smaller[b] += 1
        if smaller[b] > 1:
            check[b] = 0

for i in range(N):
    if smaller[i] == 0:
        check[i] = 0

print(sum(check))