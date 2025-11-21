N=int(input())
S = [input() for _ in range(N)]
set_ = set()
days=1
for i in S:
    if i in set_:
        continue
    else:
        print(days)
        set_.add(i)
        
    days=days+1