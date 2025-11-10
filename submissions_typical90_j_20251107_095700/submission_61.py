N = int(input())

class_1 = []
class_2 = []

for i in range(N):
  c,p = map(int,input().split(" "))
  if c == 1:
    class_1.append(p)
    class_2.append(0)
  else:
    class_1.append(0)
    class_2.append(p)