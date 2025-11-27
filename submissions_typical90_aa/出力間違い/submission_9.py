# printのresが計算間違い

N = int(input())

S = set()

res = 0

for i in range(N):

    s = input()

    if s not in S:

      S.add(s)

      res += 1

      print(res)

