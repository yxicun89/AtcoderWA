def sks(n,m):
  if m == 0:
    return n
  else:
    return sks(m,n%m)
    
i = input()
A = int(i.split()[0])
B = int(i.split()[1])
C = int(i.split()[2])
    
print(int(A/sks(A,sks(B,C))+B/sks(A,sks(B,C))+C/sks(A,sks(B,C))-3))