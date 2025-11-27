
import sys
import numpy as np

input_data = sys.stdin.read().strip().splitlines()

N = int(input_data[0])
Q = int(input_data[N + 1])

students = np.zeros((N, 2), dtype=np.int32)

for i in range(N):
    students[i] = list(map(int, input_data[i + 1].split()))

queries = np.zeros((Q, 2), dtype=np.int32)

for i in range(Q):
    queries[i] = list(map(int, input_data[N + 2 + i].split()))

scores = np.zeros((N+1, 2), dtype=np.int16)
total = np.zeros(2, dtype=np.int32)

for i in range(N):
    C, P = students[i]
    total[C-1] += P
    scores[i+1] = [total[0], total[1]]

ret = np.zeros((Q, 2), dtype=np.int32)

for i in range(Q):
    L, R = queries[i]
    ret[i] = scores[R] - scores[L-1]

for row in ret:
    sys.stdout.write(" ".join(map(str, row)) + "\n")
