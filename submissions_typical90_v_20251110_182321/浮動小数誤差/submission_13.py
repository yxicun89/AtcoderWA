s_list = list(map(int,input().split()))
s = sorted(s_list)

def f(k):
  t=k[1]%k[0]
  if t==0:
    return k[0]
  else:
    return f([t,k[0]]) # Recursive call should return the result
u=f(s[:2])
w=f([u,s[2]])
def b(a):
  return a/w
k=sum(list(map(b,s)))-3
print(int(k))