N, P, Q = map(int, input().split())
_A = list(map(int, input().split()))
A = [a % P for a in _A]
cnt = 0

for i in range(N):
	for j in range(i+1, N):
		for k in range(j+1, N):
			for l in range(k+1, N):
				for m in range(l+1, N):
					if A[i] * A[j] * A[k] * A[l] * A[m] == Q:
						cnt += 1

print(cnt)