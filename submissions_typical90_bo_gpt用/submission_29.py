def convert_8to9(str_N_8):
    num_10 = 0
    for i in range(len(str_N_8)):
        num_10 += int(str_N_8[len(str_N_8) - 1 - i]) * 8 ** i
   
    num_9 = []
    for i in range(21):
        if 9 ** i > num_10:
            continue
        num_9.append(str((num_10 // (9 ** i)) % 9))
    
    return "".join(reversed(num_9))

def replace_8to5(str_N_9):
    res = []
    for s in str_N_9:
        if s == "8":
            res.append("5")
        else:
            res.append(s)
    
    return "".join(res)

N, K = map(int,input().split())
str_N_8 = str(N)
for k in range(K):
    str_N_8 = replace_8to5(convert_8to9(str_N_8))

print(str_N_8)    