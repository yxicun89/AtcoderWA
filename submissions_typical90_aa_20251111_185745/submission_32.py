# 毎回namelistを初期化

N = int(input())

name = [input() for i in range(N)]



for i in range(N):

    namelist = []



    if name[i] not in namelist:

        print(i+1)



    namelist.append(name[i])
