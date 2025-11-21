# 条件が変
"""

競プロ典型90問_024 - Select +／- One（★2）

"""





def main():

    n, k = map(int, input().split())

    arr_a = [int(x) for x in input().split()]

    arr_b = [int(x) for x in input().split()]



    cnt = 0

    for a, b in zip(arr_a, arr_b):

        cnt += abs(a - b)



    # kと、aとbの差の、偶奇が一致するときYes

    if (cnt % 2 == 0 and k % 2 == 0) or (cnt % 2 == 1 and k % 2 == 1):

        print("Yes")

    else:

        print("No")





if __name__ == "__main__":

    main()

