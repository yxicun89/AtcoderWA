from itertools import combinations

N, P, Q = map(int, input().split())

A_list = list(map(int, input().split()))

# Pで割った余りを格納する
A = [a % P for a in A_list]

count = 0
# 総当りで試す
for combo in combinations(range(N), 5):
    
    product = 1
    
    for i in combo:
        product = product * i
        
    if product % P == Q:
        count += 1

print(count)