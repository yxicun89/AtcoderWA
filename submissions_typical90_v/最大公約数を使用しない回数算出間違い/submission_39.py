#022 - Cubic Cake（★2）

A, B, C = map(int, input().split())

while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    A = int(A/2)
    B = int(B/2)
    C = int(C/2)

ans = (A-1) + (B-1) + (C-1)
print(ans)
