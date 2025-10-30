h, w = map(int, input().split())
a = [[] for _ in range(h)]

for _ in range(h):
  a[_] = list(map(int, input().split()))
  
a_i = a
a_j = [[] for _ in range(w)]
for u in range(w):
  for v in range(h):
    a_j[u].append(a[v][u])
    
a_i_sum = []
for i in a_i:
  a_i_sum.append(sum(i))

a_j_sum = []
for j in a_j:
  a_j_sum.append(sum(j))

a_sum = [[] for _ in range(h)]
for i in range(h):
  for j in range(w):
    a_sum[i].append(a_i_sum[i] + a_j_sum[j] - a[i][j])


for i in range(h): 
    for j in range(w): 
        print(a[i][j], end=" ") 
    print()