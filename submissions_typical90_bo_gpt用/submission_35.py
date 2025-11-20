def main():
    N,K = map(int,input().split())

    for _ in range(K):
        # 10進数に
        ten_N = 0
        count = 0 # Nの桁数
        while N != 0:
            ten_N += (N%10) * (8 ** count) 
            count += 1
            N = N // 10
        # 9進数に
        nine_N = 0
        count = 0
        while ten_N != 0: 
            count += 1
            element = (ten_N % 9)
            # print(element)
            if element == 8:
                element = 5
            nine_N += element * (10 ** (count-1))
            ten_N = ten_N // 9
            # print(nine_N)
        
    print(nine_N)
        


if __name__ == "__main__":
    main()