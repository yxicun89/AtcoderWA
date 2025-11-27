import numpy as np
N,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = np.array(A)
B = np.array(B)

# A から B へ変換するのに必要な操作回数
diff = np.abs(np.sum(A - B))

# 条件判定
if diff <= K and (K - diff) % 2 == 0:
    print("Yes")
else:
    print("No")

""" if (np.sum((A-B)) - K) % 2 == 0 and (abs(np.sum((A-B))) - K) <= 0:
    print("Yes")
else:
    print("No") """
    
""" if np.sum((A-B)) == K:
    print("Yes")
elif np.sum((A-B)) % 2 == 0 and K % 2 == 0:
    print("Yes")
elif np.sum((A-B)) % 2 == 1 and K % 2 == 1:
    print("Yes")
else:
    print("No") """