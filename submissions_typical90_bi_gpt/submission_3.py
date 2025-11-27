import numpy as np

def main():
    Q = int(input())
    TX = [list(map(int, input().split())) for _ in range(Q)]
    Card = []
    for i in range(Q):
        if TX[i][0] == 1:
            Card.append(TX[i][1])
        
        elif TX[i][0] == 2:
            Card.insert(0, TX[i][1])
        
        else:
            print(Card[TX[i][1] - 1])

if __name__ == "__main__":
    main()