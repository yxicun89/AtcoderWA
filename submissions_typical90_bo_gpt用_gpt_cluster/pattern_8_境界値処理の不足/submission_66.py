def main():
    n, k = input().split()
    k = int(k)
    
    num8 = n
    for _ in range(k):
        num10 = 0
        for i in range(1, len(num8) + 1):
            num10 += int(num8[-i]) * 8 ** (i - 1)
        num8 = ''
        while num10 > 0:
            num8 = str(num10 % 9) + num8
            num10 //= 9
        num8 = num8.replace('8', '5')

    print(num8)


if __name__ == '__main__':
    main()