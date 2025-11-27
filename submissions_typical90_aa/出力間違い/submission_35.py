# 辞書順が逆

N = int(input())



userdict = {}

userlist = list()



for i in range(N):

    userlist.append(input())



for i in range(N):

    userdict[userlist[N-i-1]] = N - i



printlist = list()



for user in userdict.values():

    printlist.append(user)



printlist.reverse()



for i in range(len(printlist)):

    print(printlist[i])



