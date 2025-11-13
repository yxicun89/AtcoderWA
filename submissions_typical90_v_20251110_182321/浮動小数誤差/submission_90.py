import math
line0 = input().split(" ")

W = int(line0[0])
H= int(line0[1])
D = int(line0[2])

gcd_num = math.gcd(W,H,D)

print(int(W/gcd_num)+int(H/gcd_num)+int(D/gcd_num)-3)