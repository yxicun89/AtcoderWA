N,M=map(int,input().split())
A=[]
B=[]
co=0
from collections import defaultdict
d = defaultdict(list)
for i in range(M):
    a,b=map(int,input().split()) 
    if a<b:
        a,b=b,a
    d[b].append(a)
for i in range(N):
    if len(d[i+1])==1:
        co+=1
print(co)