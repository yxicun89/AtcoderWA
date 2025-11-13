import itertools
import math

N, P, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

am = []
for i in range(N):
  k = A[i] % P
  if k == 0:
    continue
  else:
    am.append(k)
    
count = 0
for team in itertools.combinations(am, 5):
	li = list(team)
	pr = math.prod(li)
	if pr % P ==Q:
	  count += 1
	else:
	 continue

print(count)