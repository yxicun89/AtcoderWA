
def input_str(text=None): return str(text or input())

def input_ms(text=None): return map(str, (text or input()).split(" "))

def input_mis(text=None): return map(int, (text or input()).split(" "))

def input_i(text=None): return int(text or input())

def input_lmis(text=None): return list(map(int, (text or input()).split(" ")))



N=input_i()

S_strs=[input_str() for _ in range(N)]

S_sorted_withIndex=sorted(enumerate(S_strs), key=lambda x:(x[1], x[0]))

ans_arr=[]

val_S_before=None

for ind_S, val_S in S_sorted_withIndex:

    if val_S_before==val_S:

        continue

    val_S_before=val_S

    ans_arr.append(str(ind_S+1))



ans="\n".join(map(str, sorted(ans_arr)))

print(ans)

