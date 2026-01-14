# n==0を処置できていない
n,k = map(int,input().split())

for j in range(k):
    N = 0
    for l in range(19):
        N += n%10*(8**l)
        n = n//10
        if n == 0:
            break

    s = ""
    for i in range(19):
        s = str(N%9)+s
        N = N//9
    s = s.replace("8","5")
    n = int(s)

print(n)

