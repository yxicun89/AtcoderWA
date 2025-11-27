# 最後の条件逆
n , k = map(int,input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

cou = 0

for i , j in zip(A,B):

    cou += abs(i-j)

# print(cou)

if cou > k:

    print("No")

    exit()

else:

    r = cou%2

    if r == 1:

        print("Yes")

    else:

        print("No")
