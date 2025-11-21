from itertools import combinations


def calc(p: int, q: int, an: list[int]) -> int:
    ans = 0

    for a1, a2, a3, a4, a5 in combinations(an, 5):
        if (a1 * a2 % p) * (a3 % p) * (a4 % p) * (a5 % p) == q:
            ans += 1

    return ans


def main():
    # input
    n, p, q = map(int, input().split())
    an = list(map(int, input().split()))

    # cals
    ans = calc(p, q, an)

    # answer
    print(ans)


if __name__ == "__main__":
    main()
