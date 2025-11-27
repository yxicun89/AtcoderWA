
def ri():

    i = int(input())

    return i



def rs():

    s = input()

    return s



def rl():

    line = list(map(int, input().split()))

    return line



def rls(i, rows):

    lines = [[] for n in range(rows)]



    for _ in range(i):

        line = rl()

        for n in range(rows):

            lines[n].append(line[n])



    return lines







Q = ri()

t, x = rls(Q, 2)



deck = []



for ti, xi in zip(t, x):

    if ti == 1:

        deck.insert(0, xi)

    elif ti == 2:

        deck.append(xi)

    elif ti == 3:

        print(xi)
