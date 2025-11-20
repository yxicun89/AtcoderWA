n,k=map(int, input().split())
def base_10(num_n,n):
  num_10 = 0
  for s in str(num_n):
      num_10 *= n
      num_10 += int(s)
  return num_10
def base_n(num_10,n):
  str_n = ''
  while num_10:
    if num_10%n>=10:
      return -1
    str_n += str(num_10%n)
    num_10 //= n
  return int(str_n[::-1]) if num_10!=0 else 0
for _ in range(k):
  n = str(base_n(base_10(int(n),8),9))
  n =n.replace("8","5")
print(n)