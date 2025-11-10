import pprint
N = int(input())

table = [None, [0], [0]]

for _ in range(N):
    c, p = map(int, input().split())
    for i in [1, 2]:
        table[i].append(table[i][-1] + (p if c == i else 0))
    pprint.pprint(table)

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    print(table[1][r] - table[1][l - 1], table[2][r] - table[2][l - 1])
