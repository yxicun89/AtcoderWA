dic = set()
N = int(input())
arr = [2**(7+n) for n in range(15)]
# print(arr)
count = 0
for n in range(N):
    S = ''.join(input().split())
    # print(S)
    C = [ord(s)-ord('0') for s in S]
    CC = [C[n]*arr[n] for n in range(len(S))]
    c = sum(CC)
    # print(c)
    if not c in dic:
        print(n+1)
        dic.add(c)