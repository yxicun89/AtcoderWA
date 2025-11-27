
import itertools

N,P,Q = map(int,input().split())

A = list(map(int,input().split()))

Ans = 0

for v in itertools.combinations(A,5):

    tmp = 1

    for i in range(5):

        tmp = tmp*i%P

    if tmp == Q:

        Ans+=1

print(Ans)

