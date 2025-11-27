N = int(input())

emp=["0"]*1000000
day = []
for i in range(N):
  a = input()
  l = len(a)%N
  j,c=l,0
  while c<=999999:
    if emp[j] == a:
      break
    else:
      if emp[j] == "0":
        emp[j] = a
        day.append(i+1)
        break
      else:
        if j!=N-1:
          j+=1
        else:
          j=0
      c+=1
        
for i in day:
  print(i)
  