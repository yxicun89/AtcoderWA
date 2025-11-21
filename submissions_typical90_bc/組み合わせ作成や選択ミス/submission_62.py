# i+1じゃなくてi+iになってる

def Main():

    n, p, q = map(int, input().split())

    a = list(map(int, input().split()))

    cnt = 0



    for i in range(n):

        for j in range(i + i, n):

            for k in range(j + 1, n):

                for l in range(k + 1, n):

                    for m in range(l + 1, n):

                        num = ((((a[i] * a[j]) % p * a[k]) % p * a[l]) % p * a[m]) % p

                        if num == q:

                            cnt += 1



    print(cnt)





Main()

