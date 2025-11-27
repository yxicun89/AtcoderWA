n, k = map(int, input().split())
n8_s = str(n)

for j in range(k):
    n10_i = 0
    i = 0
    for degit in n8_s:
        i += 1
        n10_i += int(degit) * 8 **(len(n8_s) - i)

    m = n10_i
    n9_s = ""
    while m > 0:
        r = m % 9
        m = m // 9
        n9_s = str(r) + n9_s

    n8_s = n9_s.replace('8', '5')

print(n8_s)