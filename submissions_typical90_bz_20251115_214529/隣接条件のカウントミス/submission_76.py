from sys import stdin
from collections import Counter

n, m = map(int, stdin.readline().split())
As = [ list(map(int, sorted(x.rstrip().split(), reverse=True)))[0] for x in stdin.readlines()]
As = Counter(As)
As = [k for k, v in Counter(As).items() if v == 1]

print(len(As))