N,k = input().split()
K = int(k)
N = list(N)[::-1]
num = 0
for i in range(len(N)):
  num += int(N[i])*(8**i) 
#print(num)
for _ in range(K):
  base_9 = []
  while num != 0:
    num,mod = divmod(num,9)
    base_9.append(mod)
  for i in range(len(base_9)):
    if base_9[i] == 8:
      base_9[i] = 5
    num += base_9[i]*(8**i)
ans = []
while num != 0:
  num,mod = divmod(num,8)
  ans.append(str(mod))
ans = ans[::-1]
print("".join(ans))