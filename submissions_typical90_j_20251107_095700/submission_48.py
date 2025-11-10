n = int(input())
scores = []
c1_sum, c2_sum = 0, 0
for _ in range(n):
    c, score = map(int, input().split())
    if c == 1:
        c1_sum += score
    else:
        c2_sum += score
    scores.append([c1_sum, c2_sum])
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    c1_l = scores[l-1][0]    
    c2_l = scores[l-1][1]
    c1_r = scores[r-1][0]
    c2_r = scores[r-1][1]
    ans_c1 = c1_r - c1_l
    ans_c2 = c2_r - c2_l
    print(ans_c1, ans_c2)