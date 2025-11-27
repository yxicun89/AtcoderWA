
def DecimalToNine(num):

  nine_number = ''

  while num > 0:

    nine_number += str(num % 9)

    num //= 9

  return int(nine_number[::-1])



n, k = map(int, input().split())

if n == 0:

  exit(print(0))



eight_number = n

for i in range(k):

  a = int(str(eight_number), 8)

  b = DecimalToNine(a)

  c = ''

  for j in range(len(str(b))):

    if str(b)[j] == '8':

      c += '5'

    else:

      c += str(b)[j]

  c = int(c)

  c = eight_number



print(eight_number)
