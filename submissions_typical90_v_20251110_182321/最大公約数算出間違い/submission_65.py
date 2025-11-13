from math import gcd

A,B,C=map(int,input().split())

gcd=gcd(gcd(A,B),B)

print(A//gcd-1+B//gcd-1+C//gcd-1)