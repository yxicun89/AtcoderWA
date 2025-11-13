Q = int(input())
l = []
m = []
for i in range(Q):
  t, x = map(int, input().split())
  #一番上入れる
  if t==1:
    l.insert(0, x)
  #一番下入れる
  elif t==2:
    l.append(x)
  #x番目出力
  else:
    n = l[x-1]
    m.append(n)
  
print(m)