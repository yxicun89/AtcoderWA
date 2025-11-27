n, k = map(int, input().split())

n = str(n)



def rewrite(n):

    ten = 0

    for i in range(len(n)):

        ten += int(n[~i]) * pow(8, i)

    nine = []

    while ten:

        if ten % 9 == 8:

            nine.append("5")

        else:

            nine.append(str(ten % 9))

        ten //= 9

    nine = "".join(nine[::-1])

    return nine



for _ in range(k):

    n = rewrite(n)



print(n)
