n, k = map(int, input().split())
ali = list(map(int, input().split()))
bli = list(map(int, input().split()))
cnt = 0

for i in range(n):
    cnt += abs(ali[i] - bli[i])

if abs(cnt-k)%2==0:
    print("Yes")
else:
    print("No")