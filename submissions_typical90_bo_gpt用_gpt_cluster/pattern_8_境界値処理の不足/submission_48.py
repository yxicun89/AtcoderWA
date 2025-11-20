N, K = input().split()
K = int(K)

def to_ten(x: str):
    x = list(x)
    x.reverse()
    rst = 0
    for dg, v in enumerate(x):
        rst += int(v) * pow(8, dg)
    return rst

def process(x: str):
    xt = to_ten(x)
    rst = []
    while xt > 0:
        d = xt % 9 
        if d == 8: d = 5 
        rst.append(str(d))
        xt //= 9
    rst.reverse() 
    return ''.join(rst)

ans = N
for _ in range(K):
    ans = process(ans)
print(ans)