N, K = map(int, input().split())

digits = list(map(int, str(N)))

def eight_to_nine(digits):

    num = 0

    for i in range(len(digits)):

        index = -1 - i

        num += digits[index] * 8 ** i

    digits = []

    while num > 0:

        digits.append(num % 9)

        num //= 9

    return digits[::-1]



for _ in range(K):

    digits = eight_to_nine(digits)

    for i in range(len(digits)):

        if digits[i] == 8:

            digits[i] = 5

print("".join(map(str, digits)))

