H,W = map(int, input().split())
list_a = [list(map(int, input().split())) for l in range(H)]
list_a_rev = [list(x) for x in zip(*list_a)]

row_sum = list(range(H))
for cnt in range(H-1):
    row_sum[cnt] = sum(list_a[cnt])

column_sum = list(range(W))
for cnt in range(W-1):
    column_sum[cnt] = sum(list_a_rev[cnt])

list_b = [[0 for i in range(W)] for j in range(H)]
for rowcnt in range(H-1):
    for columncnt in range(W-1):
        list_b[rowcnt][columncnt] = row_sum[rowcnt]+column_sum[columncnt]
