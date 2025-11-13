def main():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline

    Q = int(input())
    cards = []
    ans = []

    for _ in range(Q):
        t, x = map(int, input().split(" "))
        if t == 1:
           cards.insert(0, x)
        elif t==2:
            cards.append(x)
        else:
            ans.append(x)

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()