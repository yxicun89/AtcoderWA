Q = int(input())
INPUT = [ list(map(int, input().split())) for i in range(Q) ]
t = [ INPUT[i][0] for i in range(Q) ]
x = [ INPUT[i][1] for i in range(Q) ]
#
stack = []

# check ti (i = 0, 1, ..., Q-1)
# do operation i
for i in range(Q):
  if t[i] == 1:
    # push x[i]
    stack.append(x[i])
  if t[i] == 2:
    # insert x[i]
    stack.insert(0, x[i])
  if t[i] == 3:
    print(stack[x[i]-1])