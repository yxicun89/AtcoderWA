N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

ans = [0] * N
for a, b in AB:
    # 自分より小さい値の個数をカウントしていく
    if a < b:
        ans[b - 1] = +1
    else:
        ans[a - 1] = +1

print(ans.count(1))
