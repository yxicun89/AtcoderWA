# 半分に切っていくことを実際に行って回数計算

a_in =input()

a_in=a_in.split(" ")

a=int(a_in[0])

b=int(a_in[1])

c=int(a_in[2])

ans=0

while a!=b or b!=c or c!=a:

    if(a>=b and a>=c):

        if(a%2==1):

            ans=int(a_in[0])+int(a_in[1])+int(a_in[2])-3

            break

        else:

            a=a/2

            ans+=1

    if(b>=c and b>=a):

        if(b%2==1):

            ans=int(a_in[0])+int(a_in[1])+int(a_in[2])-3

            break

        else:

            b=b/2

            ans+=1

    if(c>=a and c>=b):

        if(c%2==1):

            ans=int(a_in[0])+int(a_in[1])+int(a_in[2])-3

            break

        else:

            c=c/2

            ans+=1

print(ans)
