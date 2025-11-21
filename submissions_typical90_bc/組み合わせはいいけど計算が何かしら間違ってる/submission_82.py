from itertools import combinations
import math

n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for item in combinations(a, 5):
    if math.prod([i % p for i in item]) == q:
        ans += 1
        
print(ans)
    
