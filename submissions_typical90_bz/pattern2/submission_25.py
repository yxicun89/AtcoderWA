NM=input().split()
N=int(NM[0])
M=int(NM[1])
newb=b=[0 for i in range(M)]
for i in range(M):
    num=input().split()
    if int(num[0])>int(num[1]):
        b[i]=int(num[0])
    else:
        b[i]=int(num[1])
counts=0
bset=set(b)

for i in bset:
    newb.remove(i)


print(len(bset)-len(newb))