# 超宇久チェックできてない

N = int(input())

names = list(input() for i in range(N))

names_set = set(names)

names_b = list(names_set)

answer = []

for  i in range(len(names_set)):

    answer.append(names.index(names_b[i])+1)

answer.sort()

print(answer)
