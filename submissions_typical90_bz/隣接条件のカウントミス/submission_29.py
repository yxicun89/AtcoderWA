import itertools # permutation
from collections import deque # queue
import heapq # priority queue

if __name__ == '__main__':
	N, M = map(int, input().split())
	G = [[] for _ in range(N+1)]
	for i in range(N+1):
		heapq.heapify(G[i])
	for _ in range(M):
		a, b = map(int, input().split())
		heapq.heappush(G[a], b)
		heapq.heappush(G[b], a)
	# print(G)
	
	ans = 0
	for i in range(1, N+1):
		if len(G[i]) == 1 and G[i][0] < i:
			ans += 1
		if 1 < len(G[i]):
			if G[i][0] < i < G[i][1]:
				ans += 1
	print(ans)
	pass
