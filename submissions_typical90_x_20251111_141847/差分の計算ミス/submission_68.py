
def solve():
    _, K = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    diff = abs(sum(A) - sum(B))

    # 最短で行動しても、合致できない場合
    if diff > K:
        print("No")
        return

    print("Yes" if (K - diff) % 2 == 0 else "No")


solve()