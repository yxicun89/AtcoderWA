n, k = map(int, input().split())

i = 0
eight_base = []
while 10**i <= n:
    eight_base.append(n//(10**i)%10)
    i += 1

for _ in range(k):
    ten_base = 0
    for i, d in enumerate(eight_base):
        ten_base += d*8**i

    nine_base = []
    while ten_base > 0:
        nine_base.append(ten_base%9)
        ten_base //= 9

    for i, d in enumerate(nine_base):
        if nine_base[i] == 8:
            nine_base[i] = 5

    eight_base = nine_base 

eight_base.reverse()
print(*eight_base, sep='')