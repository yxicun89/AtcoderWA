# 組み合わせの計算ミス

def f(selects, count):

  global di

  if 5 <= count:

    a = 0

    b = 0

    if sum(k * v for k, v in selects.items()) % P == Q:

      global ans

      a = 1

      for k, v in selects.items():

        # n!/r!*(n-r)!

        c = 1

        d = 1

        for i in range(2, di[k] + 1):

          c *= i

        for i in range(2, selects[k] + 1):

          d *= i

        for i in range(2, di[k] - selects[k] + 1):

          d *= i

        a *= c / d

      ans += a

  else:

    for i in di:

      if selects.get(i, 0) < di[i]:

        x = selects.copy()

        if i in x:

          x[i] += 1

        else:

          x[i] = 1

        f(x, count + 1)



N, P, Q = map(int, input().split())

A = [int(i)  for i in input().split()]

di = {}

ans = 0

for i in set(A):

  if i % P in di:

    di[i % P] += A.count(i)

  else:

    di[i % P] = A.count(i)

f({}, 0)

print(int(ans))
