q = int(input())

memo = [-1] * (2 * q + 1)
bottom = q
top = q


for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        if memo[top] == -1:
            memo[top] = x
            continue
        top += 1
        memo[top] = x
    elif t == 2:
        if memo[bottom] == -1:
            memo[bottom] = 1
            continue
        bottom -= 1
        memo[bottom] = x
    else:
        idx = top - x + 1
        print(memo[idx])

