# 入力
A, B, C = list(map(int, input().split()))

def find_gcd(ints):
    while len(ints) >= 2:
        min_x = min(ints)
        min_idx = ints.index(min_x)
        ints = [x % min_x if i != min_idx else x for i, x in enumerate(ints)]
        ints = [x for x in ints if x != 0]
    return ints[0]
    
gcd = find_gcd([A, B, C])

slice_cnt = (A/gcd-1) + (B/gcd-1) + (C/gcd-1)
slice_cnt = int(slice_cnt)
print(slice_cnt)