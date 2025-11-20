# 0の処理できてない

N,K=input().split()

N=list(N)

K=int(K)

for _ in range(K):

    b10=0

    N.reverse()

    for i in range(len(N)):

        b10+=8**i*int(N[i])

    b9=[]

    while b10>0:

        b9.append(b10%9)

        b10//=9

    for i in range(len(b9)):

        if b9[i]==8:

            b9[i]=5

    b9.reverse()

    N=b9

print(''.join(map(str,N)))
