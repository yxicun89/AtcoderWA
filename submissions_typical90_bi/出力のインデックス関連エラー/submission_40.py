from sys import stdin

Q = int(stdin.readline().rstrip())
tx =  [list(map(int,s.strip().split())) for s in stdin.readlines() ]

l=[]

for i in tx:
    if i[0]==1:
        l=[i[1]]+l
    elif i[0]==2:
        l.append(i[1])
    elif i[0]==3:
        print(i[1])

