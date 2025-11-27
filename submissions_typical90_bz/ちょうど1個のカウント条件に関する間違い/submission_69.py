n,m = map(int,input().split())

edge = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)
cnt = 0

for i in range(n):
    tmp = 0
    for j in range(len(edge[i])):
        if i < edge[i][j]:
            tmp += 1
            
    if tmp ==1:
        cnt +=1



# print(edge)
print(cnt)
