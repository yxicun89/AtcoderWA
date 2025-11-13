q = int(input())
deck_mae = []
deck_usiro = []
ans = []

for i in range(q):
    t,x = map(int, input().split())
    if t == 1:
        deck_mae.append(x)
    elif t == 2:
        deck_usiro.append(x)
    elif t == 3:
        if len(deck_mae) >= x:
            ans.append(deck_mae[-x])
        else:
            ans.append(deck_usiro[-(x - len(deck_mae) - 1)])

for i in ans:
    print(i)