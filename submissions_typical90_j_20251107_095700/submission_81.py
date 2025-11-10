N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
L, R = list(map(int, input().split()))

oneSum = 0
twoSum = 0

for i,a in enumerate(S):
    score = a[1]
    if a[0] == 1:
        oneSum = oneSum + score
    if a[0] == 2:
        twoSum = twoSum + score

for i,a in enumerate(S):
    score = a[1]
    if i + 1 < L or i + 1 > R:
        if a[0] == 1:
           oneSum = oneSum - score
        else:
          twoSum = twoSum - score

print(oneSum, twoSum)
