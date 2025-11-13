n =int(input())
num= [[],[]]
sum1 = 0
sum2 = 0

for i in range(n):

    c, p = map(int, input().split())
    if c == 1:
        sum1 +=p
    else:
        sum2 +=p 
    num[0].append(sum1)
    num[1].append(sum2)

q = int(input())

for i in range(q):
    l,r = map(int, input().split())
    print(num[0][r-1]-num[0][l-2],num[1][r-1]-num[1][l-2])