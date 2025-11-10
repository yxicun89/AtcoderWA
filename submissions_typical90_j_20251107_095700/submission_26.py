N = int(input())

students = []
total_A = 0
total_B = 0
for _ in range(N):
  C, P = map(int, input().split())
  if C == 1:
    total_A += P
  else:
    total_B += P
  students.append([total_A, total_B])

Q = int(input())
for _ in range(Q):
  L, R = map(int, input().split())
  score_A = students[R-1][0] - students[L-2][0]
  score_B = students[R-1][1] - students[L-2][1]
  print(score_A, score_B)
