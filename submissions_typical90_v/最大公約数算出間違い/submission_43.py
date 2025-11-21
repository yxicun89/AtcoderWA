a,b,c = list(map(int, input().split()))
x, y = a, b
r = x % y
while(x % y != 0):
    x = y
    y = r

z = c
r = z % y
while(z % y != 0):
    z = y
    y = r

ans = [(a // y) - 1, (b // y) - 1, (c // y) - 1]
print(sum(ans))