# 桁数処理ミス　これ位置で出力
N,K = map(int, input().split())



def base8to10(num):

    num = str(num)

    ret = 0

    for i in range(len(num)):

        ret += int(num[len(num)-1-i]) * 8**i

    return ret



def base10to9(num):

    num = int(num)

    ret = ""

    for i in reversed(range(20)):

        ret += str(num//9**i % 9)

    return ret



done = 0

while done != K:

    num9 = str(base10to9(base8to10(N)))

    new_base8 = ""

    for i in range(len(num9)):

        if num9[i] == "8":

            new_base8 += "5"

        else:

            new_base8 += num9[i]

    N = new_base8

    done += 1



ans = ""

zero_flg = True

for i in range(len(N)):

    if N[i] == "0":

        continue

    ans += N[i]

    if zero_flg:

        zero_flg = False

if ans == "":

    ans = "0"



print(ans)
