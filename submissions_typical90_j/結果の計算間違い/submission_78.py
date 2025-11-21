n = int(input())
class1 = [0]
class2 = [0]
for _ in range(n):
    c, p = map(int, input().split())
    if c == 1:
        class1.append(class1[-1] + p)
        class2.append(class2[-1])
    else:
        class1.append(class1[-1])
        class2.append(class2[-1] + p)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(class1[r] - class1[l -1], class1[r] - class2[l - 1])