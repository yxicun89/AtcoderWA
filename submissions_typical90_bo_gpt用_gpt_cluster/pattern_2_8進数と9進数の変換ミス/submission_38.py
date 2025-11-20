import numpy as np

def main():
    N, K = map(int, input().split())
    for _ in range(K):
        N = EtoN(N)

    print(N)
    
def EtoN(num):
    E_digits = []
    N_digits = []
    Ten = 0
    Nine = 0
    while num > 0:
        E_digits.append(num % 10)
        num //= 10
    
    for i in range(len(E_digits)):
        Ten += E_digits[i] * 8**i

    while Ten > 0:
        N_digits.append(Ten % 9)
        Ten //= 9

    for i in range(len(N_digits)):
        Nine += N_digits[i] * 9**i

    return int(str(Nine).replace("8", "5"))

if __name__ == "__main__":
    main()