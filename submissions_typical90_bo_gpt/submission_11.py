N,K = input().split()

K = int(K)



for i in range(K):

    l = len(N)

    ten = 0

    for i in range(l):

        num = int(N[i])

        ten += 8 ** (l-i-1) * num

    nine = []

    while ten > 0:

        add = ten % 9

        nine.append(str(add) if add != 8 else "5")

        ten //= 9



    N = "".join(reversed(nine))

print(N)
