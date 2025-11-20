n, k = map(int, input().split())

def make(lst):
    now = 0
    tmp = 1
    nlst = []
    while lst:
        a = lst.pop()
        now += tmp * a
        tmp *= 8
    while now:
        nlst.append(now%9)
        now //= 9
    return nlst[::-1]
n = str(n)
lst = [int(n[i]) for i in range(len(n))]
for _ in range(k):
    lst = make(lst)
    for i in range(len(lst)):
        if lst[i] == 8:
            lst[i] = 5

lst = [str(lst[i]) for i in range(len(lst))]
print("".join(lst))