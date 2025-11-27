def gcd(x, y):
    
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    if x == 0:
        return y
    else:
        return x
    
def main():
    a, b, c = map(int, input().split())
   
    # a, b, cの最大公約数を計算する
    r1 = gcd(b, c)
    r = gcd(a, r1)
    
    res = int(a/r) + int(b/r) + int(c/r) - 3
    
    print(res)

    
if __name__ == "__main__":
    main()
    