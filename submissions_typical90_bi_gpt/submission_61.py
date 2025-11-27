
q = int(input())

a = ""

for i in range(q):

  t,x = input().split()

  if t == "1":

    a = x + a

  elif t == "2":

    a = a + x

  else:

    x = int(x)

    print(int(a[x-1]))
