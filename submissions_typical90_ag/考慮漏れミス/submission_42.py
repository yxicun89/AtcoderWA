# Wを考慮できていない

H,W = map(int,input().split())

def calc(x):

  if x%2 == 0:

    ret = x//2

  else:

    ret = x//2 + 1

  return ret

if calc(H) ==1 or calc(H) ==1:

  ans = H*W

else:

  ans = calc(H)*calc(W)

print(ans)
