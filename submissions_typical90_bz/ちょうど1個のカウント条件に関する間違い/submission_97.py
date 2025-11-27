n,m=map(int,input().split())
aite=[[] for _ in range(n)]
for i in range(m):
	a,b = map(int,input().split())
	a -= 1
	b -= 1
	aite[a].append(b)
	aite[b].append(a)

for ait in aite:
	ait.sort()

counter = 0
for i in range(n):
	if ait[0] <i:
		if len(ait) == 1 or ait[1] > i:
			counter += 1
print(counter)
