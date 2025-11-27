n,k = map(int,input().split())



#1o進数toN進数

def base10int(value, base):

    if (int(value // base)):

        return base10int(int(value // base), base) + str(value % base)

    return str(value % base)



#tmpの桁の端から端まで8がないかを調べてあったら5に置き換えるという操作をk回繰り返す

for j in range(k):

    tmp = base10int(int(str(n),8),9) #8進数をを10進数に変換して10進数を9進数に変換

    tmp = tmp.replace("8","5")

    n = tmp

    print(tmp)
