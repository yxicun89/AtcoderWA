# n=0の処理漏れ

import sys



# READ_FROM_FILE = True

READ_FROM_FILE = False





def main():

    if READ_FROM_FILE:

        f = open('test0.txt', 'r')

    else:

        f = sys.stdin



    n, k = map(int, f.readline().split())

    base0 = 8

    base1 = 9

    n_list = list(map(int, str(n)))

    n_list.reverse()

    for _ in range(k):

        n = 0

        for i, d in enumerate(n_list):

            n += d * base0**i



        n_list = []

        while n > 0:

            d = n % base1

            if d == 8:

                d = 5



            n_list.append(d)

            n //= base1



    n_list.reverse()

    [print(r, end='') for r in n_list]

    print()



    if READ_FROM_FILE:

        f.close()

    return





if __name__ == '__main__':

    main()

