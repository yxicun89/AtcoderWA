N = int(input())

sums = []
suma = 0
sumb = 0

# reading and jadge
for i in range(N):
  c, p = map(int, input().split())
  if c == 1:
    suma += p
  elif c == 2:
    sumb += p  
  sums.append([suma, sumb])

# reading
Q = int(input())

# reading and calculation
for i in range(Q):
  l, r = map(int, input().split())
  tempa = sums[r-1][0] - sums[l-2][0] 
  tempb = sums[r-1][1] - sums[l-2][1] 

  print(tempa, tempb)