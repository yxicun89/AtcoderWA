n = int(input())
lc = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lq = [list(map(int, input().split())) for _ in range(q)]

#TLE
# for v in lq:
#     i = v[0] - 1
#     sum1 = 0
#     sum2 = 0
#     while i < v[1]:
#         if lc[i][0] == 1: sum1 += lc[i][1]
#         elif lc[i][0] == 2: sum2 += lc[i][1]
#         i += 1

#     print(sum1, sum2)

#学籍番号i番までの合計を求めておく
l1 = [0 for _ in range(n)]
l2 = [0 for _ in range(n)]

sum1 = 0
sum2 = 0
for i in range(n):
    if lc[i][0] == 1: sum1 += lc[i][1]
    elif lc[i][0] == 2: sum2 += lc[i][1]

    l1[i] = sum1
    l2[i] = sum2

for v in lq:
    result1 = l1[v[1]-1] - l1[v[0]-2]
    result2 = l2[v[1]-1] - l2[v[0]-2]
    
    print(result1, result2)