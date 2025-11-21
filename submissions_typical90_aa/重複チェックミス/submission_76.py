# 出力インデックス逆

N = int(input())

l_set = set()



for i in range(N):

  name = input()



  if name in l_set:

    print(i+1)

    l_set.add(name)

  else:

    pass
