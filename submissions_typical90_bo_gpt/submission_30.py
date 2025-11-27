
def base10int(value, base):

    if value == 0:

        return '0'

    if (int(value / base)):

        return base10int(int(value / base), base) + str(value % base)

    return str(value % base)



n, k = map(int, input().split())



n = str(n)

for i in range(k):

    # 8進数を10進数に

    n = int(n, 8)

    # 10進数を9進数に

    n = base10int(n, 9)



    n = n.replace('8', '5')

print(n)
