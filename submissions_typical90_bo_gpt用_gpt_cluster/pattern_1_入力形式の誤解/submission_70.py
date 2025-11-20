# 8進数として受け取ってなく10進数として処理しているミス
# このコードコメントが違うけどまず10進数を8進数に変換してるよね
# その8進数を直接9進数に変換してるミス

N, K = map(int, input().split())

M = 0


def operation(n):

  # 8進法から10進法へ

  a = 0

  k = 1

  while n > 0:

    a += (n % 10) * k

    n //= 10

    k *= 8



  # 10進法から9進法, 8を5として8進法表記へ

  b = 0

  l = 1

  while a > 0:

    b += (a % 9 if a % 9 != 8 else 5) * l

    a //= 9

    l *= 10



  return b



for i in range(1, K+1):

  N = operation(N)
