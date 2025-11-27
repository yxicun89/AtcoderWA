
H,W = map(int,input().split())



mat = []

row_sum = []

column_sum = []



for h in range(H):

    row = list(map(int,input().split()))

    row_sum.append(len(row))

    mat.append(row)



for w in range(W):

    this_column_sum = 0

    for h_ in range(H):

        this_column_sum += mat[h_][w]

    column_sum.append(this_column_sum)



for _h_ in range(H):

    for _w_ in range(W):

        num = row_sum[_h_] + column_sum[_w_] - mat[_h_][_w_]

        print(num,end="")

        if _w_ < W-1:

            print(" ",end="")

        else:

            print("")

