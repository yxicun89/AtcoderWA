n, k = input().split()
N = list(n)
K = int(k)
N.reverse()
for i in range(len(N)):
    N[i] = int(N[i])
def en(list):
    global N
    n10 = 0
    for i in range(len(N)):
        n10 += N[i] * 8**i
    N = []
    while n10:
        N.append(n10 % 9)
        n10 //= 9
    for i in range(len(N)):
        if N[i] == 8:
            N[i] = 5
    return N
for i in range(K):
    en(N)
for i in range(len(N)):
    N[i] = str(N[i])
N.reverse()
print("".join(N))
