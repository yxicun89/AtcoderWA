
N,K = map(int, input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

diff = 0

for i in range(N):

  diff += abs(A[i] - B[i])



j = True

if (diff - K) < 0:

  j = False

elif (diff - K)%2 == 1 :

  j = False



if j:

  print("Yes")

else:

  print("No")
