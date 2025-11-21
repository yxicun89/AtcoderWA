import numpy as np
n, m = map(int, input().split())
a, b = np.transpose(np.array([list(map(int, input().split())) for _ in range(m)]))
array = np.zeros((n, 1))
def max(x, y):
    if x > y:
        return x
    else :
        return y
for i in range(m):
    c = max(a[i], b[i])
    if array[c - 1] == 1:
        array[c - 1] = 0
    else:
        array[c - 1] = 1    
print(int(np.sum(array)))    