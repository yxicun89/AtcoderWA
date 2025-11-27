def ten_to_base(val, base):
    ans = []
    while val > 0:
        ans.insert(0, str(val % base))
        val //= base
    return ''.join(ans)

def eight_to_ten(val_str):
    ans = 0
    for val in val_str:
        ans = ans * 8 + int(val)
    return ans

n, k = input().split()
for i in range(int(k)):
    ten = eight_to_ten(n)
    n = ten_to_base(ten, 9)
    n = n.replace('8', '5')
print(n)
