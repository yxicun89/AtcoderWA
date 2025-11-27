def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

n,k = input().split()
k = int(k)
decimal_num = int(n,8)


for i in range(k):
    nine_num = list(base10int(decimal_num, 9))
    for j in range(len(nine_num)):
        if nine_num[j] == "8":
            nine_num[j] = "5"
    decimal_num = int("".join(nine_num),9)

print(base10int(decimal_num, 8))