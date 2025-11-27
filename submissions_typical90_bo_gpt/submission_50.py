n, k = input().split()
k = int(k)

res = 0
for i in range(len(n)):
    x = int(n[-1 - i])
    res += pow(8, i) * x

n = res
for _ in range(k):
    base9 = ""    
    for i in range(19, -1, -1):
        x = pow(9, i)
        d = n // x
        if d != 0 or len(base9) != 0:
            base9 += str(d) if d != 8 else "5"
        n %= x
    base10 = 0
    for i in range(len(base9)):
        x = int(base9[-1 - i])
        base10 += pow(8, i) * x
    n = base10
    res = base9

print(res)