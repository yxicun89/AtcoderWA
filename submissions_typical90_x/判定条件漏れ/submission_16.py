N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for a, b in zip(A, B):
    ans += abs(a - b)
    
    
if ans > K or ans == 0:
    print("No")
else:
    print("Yes")