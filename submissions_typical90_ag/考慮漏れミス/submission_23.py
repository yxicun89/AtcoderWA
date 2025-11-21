import math
H,W=map(int,input().split())

maxH = math.ceil(H/2)
maxW = math.ceil(W/2)

print(maxW*maxH)