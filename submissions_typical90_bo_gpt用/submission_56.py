def eighttoten(x):
  S=str(x)
  ans=0
  for i in range(len(S)):
    ans+=x%10*(8**i)
    x=x//10
  return ans

def tentonine(x):
  ans=""
  for i in range(18):
    ans=str(x%9)+ans
    x=x//9
  return int(ans)

N,K=map(int,input().split())
for _ in range(K):
  N=eighttoten(N)
  N=tentonine(N)
  N=int(str(N).replace('8', '5'))
print(N)