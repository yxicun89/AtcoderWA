from bisect import bisect, bisect_left


N = int(input())
S_list = []
number = []

for i in range(N):
    S_list.append(input())
for i in range(len(S_list)):
    index = bisect_left(S_list, S_list[i])
    number.append(index)
number = list(set(number))
print(*number, sep='\n')