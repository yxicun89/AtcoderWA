n = int(input())
c = [0] * n
p = [0] * n
for i in range(n):
    c[i], p[i] = map(int, input().split())
q = int(input())
l = [0] * q
r = [0] * q
for i in range(q):
    l[i], r[i] = map(int, input().split())
one = [0] * n
two = [0] * n
one_ans = 0
two_ans = 0
for i in range(n):
    if c[i] == 1:
        one[i] = p[i]
    elif c[i] == 2:
        two[i] = p[i]
#for i in range(q):
#    one_ans = sum(one[(l[i] - 1) : r[i]])
#    two_ans = sum(two[(l[i] - 1) : r[i]])
#    print(one_ans, two_ans)
