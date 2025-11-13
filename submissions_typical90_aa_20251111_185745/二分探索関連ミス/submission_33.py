# 二分探索エラー

N=int(input())

names,count=[],0

L=[]

ans=[""]

for i in range(N):

    L.append(input())



count=0

for i in range(N):

    s=L[i]

    l,r=0,count

    mid=(l+r)//2

    while l < r:

        mid=(l+r)//2

        if ans[mid] < s:

            l=mid+1

        elif s < ans[mid]:

            r=mid-1

        else:

            break

    if ans[mid]!=s:

        ans.insert(mid,s)

        count+=1

        print(i+1)

    else:

        pass

