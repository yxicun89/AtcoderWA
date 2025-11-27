H,W = map(int,input().split())

def culc(n):
  if n%2 == 1:
    return n//2+1
  return n//2

print(culc(H)*culc(W))