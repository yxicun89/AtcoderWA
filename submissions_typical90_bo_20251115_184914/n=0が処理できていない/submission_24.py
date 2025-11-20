def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

import sys
input = sys.stdin.readline

N,K = input().split()

for _ in range(int(K)):
    N = int(N,8)
    N = base10int(N,9)
    tmp = ""
    for n in N:
        if n == "8":
            n = "5"
        tmp += n
    N = tmp
        
print(N)