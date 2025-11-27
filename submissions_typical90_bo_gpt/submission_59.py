# 9進数に直す
def toNonary(n):
    s=""
    while n>0:
        k=n%9
        s=str(k)+s
        n=n//9
    return s

# 8進数を10進数に直す
# int(s, 8)でもできるが、あえて実装
def octToDec(s):
    n=0
    for c in s:
        n*=8
        n+=int(c)
    return n

def main():

    # 読み込み
    N,K = input().split()
    for _ in range(int(K)):
        N=toNonary(octToDec(N)).replace('8','5')
    print(N)

if __name__ == '__main__':
    main()
