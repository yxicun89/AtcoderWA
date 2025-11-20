# 隣接の条件が不適切

from collections import Counter

n,m=map(int,input().split())



graph =[]

for i in range(m):

    current=list(map(int,input().split()))

    if current[0]>current[1]:

        current[0],current[1]=current[1],current[0]

    graph.append(current[1])



counts=Counter(graph)#辞書形式

print(counts[1])
