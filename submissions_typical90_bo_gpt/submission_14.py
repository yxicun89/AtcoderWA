n, k = map(int, input().split())

n = str(n)



for _ in range(k):

    ten = 0

    for num in n:

        ten *= 8

        ten += int(num)

    res = []

    while ten:

        res.append(ten % 9)

        ten //= 9

    n = "".join(map(str, reversed(res))).replace("8", "5")

print(n)

