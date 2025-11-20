# 再帰関数でオーバーフロー

def LI(): return list(map(int, input().split()))

def II(): return int(input())

from math import floor



N,K=LI()

N=str(N)



#10進数からn進数へ変換

def base10int(value, base):

    if floor(value / base):

        return base10int(floor(value / base), base) + str(value % base)

    return str(value % base)





for _ in range(K):

    base10 = int(N, 8)

    base9 = base10int(base10, 9)

    while (len(base9)>1 and base9[0]=="0"): base9=base9[1:]



    N = base9.replace("8", "5")



print(N)
