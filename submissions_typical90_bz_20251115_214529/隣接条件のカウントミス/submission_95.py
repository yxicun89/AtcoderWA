n,m=map(int,input().split())
Tree =[0] *n
for i in range(m):
  b =min(map(int,input().split()))
  Tree[b-1] +=1
ans =0
print(Tree.count(1))