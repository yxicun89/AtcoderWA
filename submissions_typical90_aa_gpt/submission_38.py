# iではなくtmpを出力している

N=int(input())



inputs =[]

for i in range(N):

    tmp =input()

    if tmp in inputs:

       tmp =tmp

    else:

      inputs.append(tmp)

      print(tmp)
