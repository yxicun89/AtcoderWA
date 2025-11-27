user=[]

n=int(input())

for i in range(n):

  name=input()

  if name in user:

    continue

  user.append(name)

  print(i)
