import bisect

N = int(input())

S = []

for i in range(N):

  X = input()

  ind = bisect.bisect_left(S, X)

  ind_ = bisect.bisect_right(S, X)

  if ind != ind_:

    print(i+1)

    S.append(X)

    S.sort()

