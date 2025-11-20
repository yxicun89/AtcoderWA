
q = int(input())

deck = [0]*(q*2+4)

deckdraw = []

c = q+2

right = c

left = c-1



for i in range(q):

    t, x = map(int, input().split())

    if t == 3:

      deckdraw.append(x)

    elif t == 2:

      deck[left] = x

      left -= 1

    else:

      deck[right] = x

      right += 1



for i in deckdraw:

    print(deck[right-i])









