
from math import ceil



H, W = map(int, input().split())



h_max = ceil(H / 2)

w_max = ceil(W / 2)

print(h_max * w_max)

