# not inじゃなくて in になってる

n = int(input())

list = []

for i in range(n):

  id = input()

  if id in list:

    list.append(id)

    print (i+1)
