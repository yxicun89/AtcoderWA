# クエリ処理できてない
if __name__ == '__main__':
  N = int(input())
  
  sum1 = [0] * (N+1)
  sum2 = [0] * (N+1)
  for i in range(1, N + 1):
    c, p = map(int, input().split())
    sum1[i] = sum1[i - 1]
    sum2[i] = sum2[i - 1]
    if c == 1:
      sum1[i] += p
    else:
      sum2[i] += p