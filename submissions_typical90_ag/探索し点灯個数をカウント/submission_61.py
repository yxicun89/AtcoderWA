def notTooBright(H: int, W: int) -> int:
    dp = [[False] * (W + 1) for _ in range(H + 1)]
    total = 0
    for r in range(1, H + 1):
        for c in range(1, W + 1):
            # Can place LED at (r, c) only if no LEDs in the top-left 2x2 square
            if not dp[r - 1][c - 1] and not dp[r - 1][c] and not dp[r][c - 1]:
                dp[r][c] = True
                total += 1
    return total

def main():
    H, W = map(int, input().split())
    print(notTooBright(H, W))

if __name__ == "__main__":
    main()