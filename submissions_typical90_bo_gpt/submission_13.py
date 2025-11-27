def to_decimal(x):

  ret = 0

  for i, num in enumerate(x[::-1]):

    ret += int(num) * pow(8, i)

  return ret



def to_nine(x):

  ret = []

  while x > 0:

    ret.append(str(5 if x % 9 == 8 else x % 9))

    x //= 9

  ret.reverse()

  return "".join(ret)



N, K = input().split()



for _ in range(int(K)):

  N = to_decimal(N)

  N = to_nine(N)



print(N)
