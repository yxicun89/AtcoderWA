N = int(input())



user = set(['a'])

for i in range(N):

  s = input()

  if s not in user:

    print(i + 1)

    user.add(s)
