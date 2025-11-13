import itertools

N,P,Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a1,a2,a3,a4,a5 in itertools.combinations(A,5):
  if (a1%P)*(a2%P)*(a3%P)*(a4%P)*(a5%P) == Q:
    ans += 1
print(ans)