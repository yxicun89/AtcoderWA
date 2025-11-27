
n = int(input())
test_result = []
for i in range(n):
    test_result.append(tuple(map(int, input().split())))
q = int(input())
querys = []
for i in range(q):
    querys.append(tuple(map(int, input().split())))

for nim_num, max_num in querys:
    sum1, sum2 = (0, 0)
    for l, r in zip(range(nim_num - 1, 100000), range(max_num - 1, 0, -1)):
        if l > r:
            break
        elif l == r:
            if test_result[l][0] == 1:
                sum1 += test_result[l][1]
            else:
                sum2 += test_result[l][1]
        else:
            if test_result[l][0] == 1:
                sum1 += test_result[l][1]
            elif test_result[l][0] == 2:
                sum2 += test_result[l][1]

            if test_result[r][0] == 1:
                sum1 += test_result[r][1]
            elif test_result[r][0] == 2:
                sum2 += test_result[r][1]


    print(sum1, sum2)
