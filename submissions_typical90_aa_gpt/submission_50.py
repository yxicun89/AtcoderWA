num = int(input())

lis = []

count = 0

set_foward = 0

for i in range(num):

  lis.append(input())

s_lis = set(lis)

for j in s_lis:

  print(lis.index(j) + 1)
