# set定義していないから毎回空になる

N=int(input())



for i in range(N):

    s=input()

    if s in set():

        continue

    set().add(s)

    print(i+1)

