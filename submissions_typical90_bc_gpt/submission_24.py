import itertools

N,P,Q=map(int,input().split())

A=list(map(int,input().split()))



ans=0

for comb in itertools.combinations(A, 5):

    if (comb[0]*comb[1]+comb[2])*comb[3]%P==Q:

        ans+=1

print(ans)
