N = int(input())
S = []
T = []
totals = 0
totalt = 0
S.append(totals)
T.append(totalt)
for i in range(N):
	c, p = map(int, input().split())
	if c == 1:
		totals += p
	else:
		totalt += p
	S.append(totals)
	T.append(totalt)
Q = int(input())
for j in range(Q):
	l, r = map(int, input().split())
	a = S[r]-S[l-1]
	b = T[r]-T[l-2]
	print(a, b)