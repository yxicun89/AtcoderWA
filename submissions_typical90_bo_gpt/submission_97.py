def num8to10(n):
    sum = 0
    for a, b in enumerate(reversed(n)):
        sum += int(b) * (8 ** a)
    return sum
        
def num10to9(n):
    p = []
    while n > 0:
        a = n % 9
        p.insert(0, a)
        n = n // 9
    return ''.join(map(str, p))  # 最後に一度だけ文字列に変換

def num8wo5(n): 
    n = list(n)  # 文字列をリストに変換
    for i in range(len(n)):
        if n[i] == "8":
            n[i] = "5"
    return ''.join(n)  # リストを文字列に戻す

def moji(n):
    return ''.join(map(str, n))

if __name__ == "__main__":
    A = input("Enter a number and iterations: ").split()
    a = A[0]

    for i in range(int(A[1])):
        a = str(num8to10(a))  # 整数を文字列に変換
        a = num10to9(int(a))  # 文字列を整数に変換
        a = num8wo5(a)
        a = moji(a)  # この関数呼び出しは冗長

    print(a)
