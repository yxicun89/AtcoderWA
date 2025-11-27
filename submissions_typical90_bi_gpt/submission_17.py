Q = int(input())
cards = []

for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        cards.append(x)
        
    elif t == 2:
        cards.insert(0, x)
    else:
        print(list[-x])
