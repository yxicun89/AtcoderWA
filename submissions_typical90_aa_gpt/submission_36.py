
N = int(input())

userlist = []

anslist = []

for i in range(N):

    u = input()

    if (u not in userlist):

        anslist.append(i+1)

    else:

        userlist.append(u)



for x in anslist:

    print(x)
