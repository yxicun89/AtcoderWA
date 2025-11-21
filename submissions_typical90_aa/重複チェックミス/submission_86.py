#027 - Sign Up Requests （★2）

N=int(input())

S=list(range(N))

for i in range(N):

    S[i]=input()

    if len(S)!=len(set(S)):

        S=list(set(S))

        S.append(int(N+i))

        continue

    print(i+1)
