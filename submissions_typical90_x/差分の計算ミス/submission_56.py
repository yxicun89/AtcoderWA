# 差分の計算ミス
import sys



def main():

    N,K=map(int,sys.stdin.readline().split())

    A=list(map(int,sys.stdin.readline().split()))

    B=list(map(int,sys.stdin.readline().split()))



    d=abs(sum(A)-sum(B))

    print("Yes" if d<=K and (d-K)%2==0 else "No")



if __name__ == "__main__":

    main()
