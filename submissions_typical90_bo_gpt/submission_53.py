n, k = map(int, input().split())
n = str(n)
for i in range(k):
    n10 = 0
    n9 = ""
    for j in range(len(n)):
        n10 += int(n[len(n)-j-1])*(8**j)
    a9 = 1
    while n10 >= a9:
        a9 *= 9
    while a9 >= 1:
        n9 += str(int(n10//a9))
        n10 = n10 % a9
        a9 /= 9
    n9 = n9.replace("8", "5")
    n = str(int(n9))
print(n)
