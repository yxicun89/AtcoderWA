N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for i in range(len(A)):
    ans+=abs(A[i]-B[i])
if A==B:
    if K%2==0:
        print("Yes")
    else:
     print("No")
    exit()
if K==ans:
    print("Yes")
elif K<ans:
    if (K-ans)%2==0:
        print("Yes")
    else:
      print("No")
else:
   print("No")