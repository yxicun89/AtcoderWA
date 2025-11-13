def main():
  
  N = int(input())
  
  C = N*[0]
  P = N*[0]
  for i in range(N):

    temp = input().split()
    c = int(temp[0])
    p = int(temp[1])
    
    C[i] = c
    P[i] = p

  Q = int(input())
  L = Q*[0]
  R = Q*[0]
  for i in range(Q):

    temp = input().split()
    l = int(temp[0])
    r = int(temp[1])
    
    L[i] = c
    R[i] = r
  
  for i in range(Q):
    
    class1 = 0
    class2 = 0
    
    for j in range(L[i], R[i]+1):
      
      if C[j-1]==1:
        class1 += P[j-1]
        
      elif C[j-1]==2:
        class2 += P[j-1]
        
    print(class1, class2)
  
  return


if __name__=="__main__":
  
  main()