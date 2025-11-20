N, K = input().split(" ")
K = int(K)

for i in range(K):
    n = 0
    for j in range(len(N)):
            n += int(N[-1-j])*(8**j)
    N = []
    while n != 0:
          x = n % 9
          N.insert(0,str(x))
          n //= 9
    for i in range(len(N)):
          if N[i] == "8":
                N[i] = "5"
    N = "".join(N)
print(N)