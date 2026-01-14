# 出力タイミングミス
n,k = map(int,input().split())

def base10int(value, base):
    if (int(value // base)):
        return base10int(int(value // base), base) + str(value % base)
    return str(value % base)

for j in range(k):
    tmp = base10int(int(str(n),8),9)
    tmp = tmp.replace("8","5")
    n = tmp
    print(tmp)
