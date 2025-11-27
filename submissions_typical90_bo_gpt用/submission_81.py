\
n_base8, k = map(int, input().split())



for _ in range(k):

    # print(n_base8)

    n_base8 = str(n_base8)

    n_base10 = 0

    for i in range(len(n_base8)):

        n_base10 += int(n_base8[i]) * (8 ** (len(n_base8)-i-1))

    # print(n_base10)

    n_base9 = ""

    flag = True

    for i in range(100, -1, -1):

        if 9**i > n_base10 and flag:

            continue

        flag = False

        if n_base10 // (9**i) == 0:

            n_base9 = n_base9 + '0'

            continue

        n_base9 = n_base9 + str(n_base10 // (9**i))

        n_base10 = n_base10 % (9**i)

    n_base9 = list(n_base9)

    for i in range(len(n_base9)):

        if n_base9[i] == '8':

            n_base9[i] = '5'

    n_base8 = ''.join(n_base9)

n_base9 = ''.join(n_base9)

print(n_base9)
