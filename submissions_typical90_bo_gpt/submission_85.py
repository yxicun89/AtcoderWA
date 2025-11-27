n,k = map(int,input().split())
for i in range(k):
    ei = 0
    ni = ''
    for j in range(len(str(n))):
        ei += int(str(n)[-1-j]) * (8 ** j)

    while(ei // 9 >= 1):
        ni = str(ei % 9) + ni
        ei //= 9

    ni = str(ei) + ni
    ni = ni.replace('8','5')

print(ni)