
# 061 -Deck(2)

q = int(input())

x_list = [0]*q

top = 0

bottom = 0

for _ in range(q):

    t, x = map(int, input().split())

    if t == 1:

        x_list[top] = x

        if top == 0:

            bottom += 1

        top -= 1

    if t == 2:

        x_list[bottom] = x

        bottom += 1

    if t == 3:

        print(x_list[x+top])







