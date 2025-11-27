n,k = input().split()
n_a = n
for _ in range(int(k)):
  x = 1
  tmp = 0
  A = []
  for i in range(1,len(n_a)+1):
    tmp += int(n_a[-i]) * x
    x *= 8
 
  while tmp > 0:
    kyu = tmp % 9
   
    if kyu == 8:
      kyu = 5
    A.append(kyu)
   
    tmp //= 9 
  
  A.reverse()
  n_a = "".join(map(str,A))
print(n_a)