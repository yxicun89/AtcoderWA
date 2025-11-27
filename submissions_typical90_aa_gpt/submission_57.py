n = int(input())
list = []

for i in range(n):
  s = str(input())
  if s not in(list):
    list.append(s)
    print(i)