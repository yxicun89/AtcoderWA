from sys import stdin


N,M = [list(map(int,s.strip().split())) for s in stdin.readline().rstrip().split()]
AB = [list(map(int,s.strip().split())) for s in stdin.readlines() ]
count =0
for i in AB:
    max_i = max(i)
    for m in AB:
        if max_i in m and max_i*2 >sum(m):
            break
    else:
        count +=1
print(count) 
            
        