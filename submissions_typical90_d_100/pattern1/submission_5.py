# 累積和使ってない

hw = input()

h, w = hw.split(' ')

h = int(h)

w = int(w)



t = []



for _ in range(h):

    i = input()

    line = [int(n) for n in i.split(' ')]

    t.append(line)



rev_t = [list(x) for x in zip(*t)]  # 転置



result = []



for line_indx, line in enumerate(t):  # まず列を足す

    line_total = sum(line)

    line_result = []



    for idx, num in enumerate(line):

        col_total = sum(rev_t[idx])



        line_result.append(line_total + col_total - num)



    print(line_result)

