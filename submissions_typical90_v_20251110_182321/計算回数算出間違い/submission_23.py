import numpy as np
from functools import reduce

def main():
    A, B, C = map(int, input().split())

    # NumPyのgcdを使って3つの数の最大公約数を求める
    G = reduce(np.gcd, [A, B, C])

    # 各辺をGで割って、何個に分けられるか（整数除算）
    diffA = A // G
    diffB = B // G
    diffC = C // G

    # 最終的な出力をint型にしてprint（np.int64だとWAになることがある）
    result = int(diffA * diffB * diffC - 1)
    print(result)

if __name__ == "__main__":
    main()
