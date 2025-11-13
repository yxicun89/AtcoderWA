import math

A,B,C = input().split()

G = math.gcd(int(A), int(B))
G = math.gcd(G, int(C))

print(int(int(A)/G + int(B)/G + int(C)/G -3))