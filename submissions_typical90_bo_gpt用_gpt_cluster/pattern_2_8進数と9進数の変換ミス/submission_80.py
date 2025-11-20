_N,_K = input().split()
K = int(_K)
N_9 = list(map(int,list(_N)))[::-1]

for _ in range(K):
    N = sum([N_9[i]*8**i for i in range(len(N_9))])
    # print(N)
    N_9 = []
    t = N
    while t > 0:
        N_9.append(t%9)
        t //= 9
    # print(N_9)
    for i in range(len(N_9)):
        N_9[i] = 5 if N_9[i] == 8 else N_9[i]
    # print(N_9)

s = ""
for i in range(len(N_9)):
    s += str(N_9[::-1][i])
print(s)