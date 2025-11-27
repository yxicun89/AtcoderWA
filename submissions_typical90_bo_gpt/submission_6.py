import sys



n, k = list(map(int, sys.stdin.readline().split()))

n = str(n)

for _ in range(k):

    m = 0

    for i in range(len(n)):

        m += int(n[-i - 1]) * 8**i

    k = []

    while not m < 9:

        m, a = divmod(m, 9)

        if a == 8:

            k.append(5)

        else:

            k.append(a)

    if k == 8:

        k.append(5)

    else:

        k.append(m)

    n = "".join(map(str, list(reversed(k))))

print(n)

