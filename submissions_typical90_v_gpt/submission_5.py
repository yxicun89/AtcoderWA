
a, b, c = map(int, input().split())



x = 1

while a % (x*2) == 0 and b % (x*2) == 0 and c % (x*2) == 0:

  x *= 2



print(a//x + b//x + c//x - 3)
