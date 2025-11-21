
import sys
import math

def main():
    input = sys.stdin.readline
    H, W = map(int,input().split())

    answer = ((H+1)//2) * ((W+1)//2)
    print(answer)


if __name__ == "__main__":
    main()



