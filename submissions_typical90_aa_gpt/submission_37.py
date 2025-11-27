# whileの条件エラー

N=int(input())

lst=[]

ilst=[]

for i in range(1,N+1):

    lst.append(input())

    ilst.append([lst[i-1],i])



lst=sorted(list(set(lst)))

ilst=sorted(ilst)

index=0

i=0

ans=[]

for i in lst:

    while index<N:

        if i==ilst[index][0]:

            ans.append(ilst[index][1])

            break

        index+=1

print(sorted(ans))
