
N=int(input())

dic=dict()

for i in range(1,N+1):

    S=str(input())

    if S not in dic:

        dic[i]=S

        print(i)

    else:

        pass
