N,K = input().split()

K = int(K)



def base8to9(base8):

  num_10 = 0

  for i in range(len(base8)):

    n = int(base8[i])

    num_10 += n*(8**(len(base8)-1-i))



  base9 = ''

  while(num_10 != 0):

    base9 = str(num_10%9)+base9

    num_10 //= 9



  return base9



def change8to5(base9):

  return base9.replace('8','5')



for _ in range(K):

  N = base8to9(N)

  N = change8to5(N)



print(N)
