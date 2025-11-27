n, k = input().split()

crr = n

for _ in range(int(k)):

    # 8 -> 10

    crr = sum(int(num) * 8**idx for idx, num in enumerate(crr[::-1]))

    # 10 -> 9

    temp = []

    while crr > 0:

        crr, m = divmod(crr, 9)

        temp.append(m if m != 8 else 5)



    crr = "".join(map(str, temp[::-1]))



print(crr)

