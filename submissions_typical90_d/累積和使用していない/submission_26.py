#004 Cross Sum - Lv.2

H, W = map(int, input().split())
cross = [list(map(int, input().split())) for row in range(H)]

for h in range(H):
    for w in range(W):
        hsum = sum(cross[h])
        wsum = 0
        for h in range(H):
            wsum += cross[h][w]
        print(hsum + wsum - cross[h][w], end=" ")
    print()