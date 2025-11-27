
import sys

import itertools





def main():

    inputs = [list(map(int, line.split(u' ')))

              if u' ' in line.strip() else int(line.strip())

              for line in sys.stdin.read().strip().split('\n')]

    N, P, Q = inputs[0]

    Q5 = Q**5

    A = inputs[1]

    mods = [a % P for a in A]



    c = 0

    for v in itertools.combinations(mods, 5):

        if v[0]*v[1]*v[2]*v[3]*v[4] == Q:

            c += 1

    print(c)



if __name__ == '__main__':

    main()

