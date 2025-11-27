def convert(n, base):
    res = ""
    while n > 0:
        res = str(n%base) + res
        n //= base
    return res


def re_convert(n, base):
    res = 0
    for i in range(len(n)):
        res += int(n[i]) * (base**(len(n)-i-1))
    return res


N, K = map(int, input().split())

for _ in range(K):
    N = re_convert(str(N), 8)
    N = convert(N, 9)
    tmp = ""
    for n in N:
        if n == "8":
            tmp += "5"
        else:
            tmp += n
    N = tmp

print(N)
