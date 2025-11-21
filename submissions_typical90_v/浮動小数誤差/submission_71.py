A,B,C = map(int,input().split())
def gcd(x,y):
  a = max(x,y)
  b = min(x,y)
  while b !=0:
    c = a%b
    a = b
    b = c
    if b ==1:
      return 1
      break
  return a

ans = gcd(A,gcd(B,C))
print(int(A/ans) + int(B/ans) + int(C/ans) -3)

