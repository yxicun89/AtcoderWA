# 計算回数算出間違い

MOD = 10**9 + 7

def cubicCake(a: int, b: int, c: int, mod: int = MOD) -> int:

  def gcd(x: int, y: int) -> int:

    if x < y:

      return gcd(y, x)

    if y == 0:

      return x

    return gcd(y, x%y)

  cnt = gcd(a, gcd(c, b))

  total_cnt = ((a // cnt -1 ) % mod + (b // cnt - 1) % mod + (c // cnt - 1) % mod) % mod



  return total_cnt



def main():

  a, b, c = map(int, input().split())

  ans = cubicCake(a, b, c, MOD)

  print(ans)



if __name__ == "__main__":

  main()
