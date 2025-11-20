N, K = input().split()
K = int(K)

def to10(s):
    res = 0
    n = len(s)
    for i in range(n):
        res *= 8
        res += int(s[i])
    return res

def to9(x):
    res = ""
    while x > 0:
        r = x%9
        res += str(r)
        x //= 9
    return res[::-1]

def trans8to5(s):
    res = ""
    n = len(s)
    for i in range(n):
        if s[i] == "8":
            res += "5"
        else:
            res += s[i]
    return res

for i in range(K):
    N = trans8to5(to9(to10(N)))

print(N)




