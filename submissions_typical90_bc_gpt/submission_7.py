from itertools import combinations

n,p,q=map(int,input().split())

a=list(map(int,input().split()))

ans=0

for data in combinations(list(range(n)),5):

    pro=1

    for a in data:

        pro=(pro*a)%p

    if pro==q:

        ans+=1

print(ans)
