# 1の場合考慮してるけどreturn 0

def max_led_num(h, w):

    if h == 1 or w == 1:

        return 0

    h2 = h + 1 if h % 2 == 1 else h

    w2 = w + 1 if w % 2 == 1 else w

    return (h2 * w2) // 4



def main():

    h, w = map(int, input().split())

    print(max_led_num(h, w))



if __name__ == "__main__":

    main()

