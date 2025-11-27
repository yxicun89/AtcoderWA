def base10int(value):
    if (int(value / 9)):
        return base10int(int(value/9))+str(value % 9)
    return str(value % 9)

def base8to9(value):
    ret = int(str(value),8)
    ret = int(base10int(ret))
    return ret

def str8to5(value):
    value = str(value)
    rev = ""
    for i in range(len(value)):
        if value[i] == "8":
            rev += "5"
        else:
            rev += value[i]
    rev = int(rev)
    return rev

N,K = map(int,input().split())
for i in range(K):
    N = str8to5(base8to9(N))
print(N)