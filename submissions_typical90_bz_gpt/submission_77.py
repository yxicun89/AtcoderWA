from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

inp = [list(map(int, stdin.readline().rstrip().split())) for i in range(int(M))]
lis =[inp[i][0] if inp[i][0] < inp[i][1] else inp[i][1] for i in range(int(M))]
se =set(lis)
answer = [lis[i] for i in range(len(lis)) if not lis[i] in se]

print(len(answer))