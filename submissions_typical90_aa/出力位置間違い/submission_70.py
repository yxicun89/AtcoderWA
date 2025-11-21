import sys
input = sys.stdin.readline

name = set()
N = int(input())

for i in range(N):
    s = input()
    if (s in name):
        continue
    else:
        name.add(s)
        print("{}".format(i))