# 入力したものではなく文字列sを格納してる

n = int(input())

a =[]

for i in range(1,n+1):

    s =input()

    if s not in a:

        a.append("s")

        print(i)

