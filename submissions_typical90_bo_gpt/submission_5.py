def eight_to_ten(n):

    res = 0

    for i in range(len(n)):

        res += int(n[len(n)-1-i])*(8**i)

    return res



def ten_to_nine(n):

    res = ""

    while n > 0:

        res = str(n%9) + res

        n //= 9

    return res



def replace_eight(n):

    return n.replace("8","5")





n,k = map(int, input().split())

for _ in range(k):

    n = eight_to_ten(str(n))

    n = ten_to_nine(n)

    n = replace_eight(n)



print(n)
