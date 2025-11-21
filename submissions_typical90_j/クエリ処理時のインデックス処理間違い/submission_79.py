N = int(input())
class_1 = [0] * (N + 1)
class_2 = [0] * (N + 1)

for i in range(1, N+1):
    class_1[i], class_2[i] = class_1[i-1], class_2[i-1]
    C, P = map(int, input().split())
    if C == 1:
        class_1[i] += P
    else:
        class_2[i] += P

Q = int(input())
for _ in range(Q):
    L, R =map(int, input().split())
    print(class_1[R] - class_1[L], class_2[R] - class_2[L])
