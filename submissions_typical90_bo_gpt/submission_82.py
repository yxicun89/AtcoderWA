import decimal

N, K = input().split()

list_N = [0]*(20-len(N)) + [int(N[i]) for i in range(len(N))]

flag=0
min_index=20

for i in range(20):
  if list_N[i] !=0:
    min_index=i
    break

n_temp = sum([list_N[i]*(8**(19-i)) for i in range(min_index,20)])
K = int(K)

for k in range(K):
  if min_index>=19:
    break
  for i in range(min_index,20):
    q = int(decimal.Decimal(n_temp) // decimal.Decimal(9**(19-i)))
    n_temp = int(decimal.Decimal(n_temp) % decimal.Decimal(9**(19-i)))
    if q==8:
      list_N[i] = 5
    else:
      list_N[i] = q
  for i in range(min_index,20):
    if list_N[i] !=0:
      min_index=i
      break
  n_temp = sum([list_N[j]*(8**(19-j)) for j in range(min_index,20)])

list_N = list_N[min_index:]
list_N = list(map(str,list_N))

print(''.join(list_N))