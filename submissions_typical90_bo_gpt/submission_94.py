from collections import deque
n,k = map(int,input().split())
n = str(n)
def f(base8):
    cnt = 0
    for i in range(len(base8)):
        cnt += int(base8[-1-i])*(8**i)
    a = cnt
    base9 = deque()
    while a != 0:
        a,d = divmod(a,9)
        base9.appendleft(d)
    
    for i in range(len(base9)):
        if base9[i] == 8:
            base9[i] = 5
    ans = "".join(map(str,base9))
    return ans



for _ in range(k):
    n = f(str(n))

print(n)