a, b, c = map(int, input().split())

while True:
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        a //= 2
        b //= 2
        c //= 2
    else:
        break

print(a+b+c-3)