import math


def convert_to_base(num, before_base, after_base):
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * pow(before_base, len(num)-i-1)
        # print(f'decimal={decimal}')
    result = ''
    while (decimal > 0):
        digit = decimal % after_base
        # print(f'digit={digit}')
        decimal = decimal // after_base
        result = str(digit) + result
    # print(f'ctb result = {result}')
    return result


def eight_to_five(num):
    num = str(num)
    new_num = []
    for char in num:
        if (char == '8'):
            new_num.append('5')
        else:
            new_num.append(char)
    # print(f'etf result = {num}')
    return ''.join(new_num)


N, K = map(str, input().split())
K = int(K)

for i in range(K):
    N = eight_to_five(convert_to_base(N, 8, 9))

print(N)
