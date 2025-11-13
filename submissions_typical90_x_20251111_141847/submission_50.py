# k以下じゃなくてn以下になってる

import numpy as np

n,k=map(int,input().split())

a=np.array(input().split(),dtype=int)

b=np.array(input().split(),dtype=int)

dif = sum(abs(a-b))

if dif<=n:

  print("Yes" if k%2 == dif%2 else "No")

else:

  print("No")
