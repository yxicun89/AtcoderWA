def LI(): return list(map(int, input().split()))
def II(): return int(input())

N,K=LI()
N=str(N)

#10進数からn進数へ変換
def base10int(value, base):
    if value // base:
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

for _ in range(K):
    base10 = int(N, 8)
    base9 = base10int(base10, 9)

    N = base9.replace("8", "5")
    
print(N)