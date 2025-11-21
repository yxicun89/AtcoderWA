def solve(h: int, w: int) -> int:
    if h % 2:
        h += 1
    if w % 2:
        w += 1
    return (h // 2) * (w // 2)


h, w = map(int, input().split())
ans = solve(h, w)
print(ans)
