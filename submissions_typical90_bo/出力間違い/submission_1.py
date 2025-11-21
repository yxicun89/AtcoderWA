# 置き換え処理が本来反映させたいリストに反映されていない
# nを更新できていない
# 変換処理間違い

n,k=map(int,input().split())

n=str(n)

n=list(n)

for times in range(k):

    ans=0

    n.reverse()

    for i in range(len(n)):

        ans+=8**(i)*int(n[i])

    nine=[]

    #print(ans)

    while ans!=0:

        nine.append(ans%9)

        ans=ans//9

    nine.reverse()

    n=nine

    #print(nine)

    for i in range(len(nine)):

        if nine[i]==8:

            nine[i]=5

#print(nine)

lastans=[]

for i in nine:

    lastans.append(str(i))

print("".join(lastans))





