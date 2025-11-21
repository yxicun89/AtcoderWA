n = int(input())
points_1 = {}
points_2 = {}

for  i in range(1, n+1):
    a, b = map(int, input().split())
    if a == 1:
        points_1[i] = b
    else:
        points_2[i] = b

q = int(input())
res = []

for _ in range(q):
    a, b = map(int, input().split())
    stu = a
    cnt = 1
    p1 = 0
    p2 = 0
    res = []
    while cnt <= b - a + 1:
        try:
            p1 +=  points_1[stu]
        except:
            p2 += points_2[stu]
        finally:
            cnt += 1
            stu += 1
    res.append([p1, p2])

for l in res:
    print(*l)
            
            
            

