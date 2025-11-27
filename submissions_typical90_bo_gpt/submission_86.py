N, K = input().split()

for k in range(int(K)):
    n = 0
    for i in range(len(N)):
        n += int(N[-i-1]) * 8**i
    nine = ""
    while n > 0:
        nine = str(n % 9) + nine
        n //= 9
    eight = ""
    for s in nine:
        eight += s if s != "8" else "5"
    N = eight
print(N)