# 競プロ典型90 - 022
inp = list(map(int, input().split()))
a = inp[0]
b = inp[1]
c = inp[2]

i = 1
while a % (i*2) == 0 and b % (i*2) == 0 and c % (i*2) == 0:
    i = i * 2
    
a = a // i
b = b // i
c = c // i

min_value = min(a, b, c)
if a % min_value == 0 and b % min_value == 0 and c % min_value == 0:
    a = a // min_value
    b = b // min_value
    c = c // min_value

print(a + b + c - 3)