
N = int(input())

S_set = set()

for i in range(1,N):

    s = input()

    if s in S_set:

        continue

    else:

        print(str(i))

        S_set.add(s)



