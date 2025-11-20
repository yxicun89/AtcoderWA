#2025/8/27

#典型90問_0067 - Base 8 to 9（★2）



N,K=map(int,input().split())



N=list(str(N))







for j in range(K):

    ten=0

    nine=0

    keta=len(N)

    for i in range(keta):

        ten+=(8**(keta-i-1)*int(N[i]))



    keta2=len(str(ten))

    for i in range(keta2):

        nine+=ten%9*10**i

        ten=ten//9



    N=list(str(nine).replace("8","5"))



print("".join(N))
