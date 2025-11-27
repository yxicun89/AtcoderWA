import sys
import os
# 再帰関数の上限を増やす
sys.setrecursionlimit(10**7)
# 入力を高速にする"まじない"
input = lambda: sys.stdin.readline().rstrip()
# ローカル環境で実行するときに input.txt を標準入力にする
# os.path.exists('input.txt') でファイルが存在するかチェック
filename = r'競プロ典型問題90\インプットファイル\024_input.txt'
if os.path.exists(filename):
    sys.stdin = open(filename, 'r')

# PyPy3環境で再帰を高速化する
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

def MAPIN():
    return map(int,input().split())
def LIN():
    return list(map(int,input().split()))

# ---ここから---------------------------------------------
N,K = MAPIN()
A = LIN()
B = LIN()

M = 0
for i in range(N):
    M += abs(A[i]-B[i])
print(M)

if (K%2 == M%2) and (K >= M):
    print("Yes")
else:
    print("No")