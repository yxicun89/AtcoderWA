import io
import sys




n = int(input())  #生徒の数

kumi=[]
score=[]
for i in range(n):
    k,s = (map(int, input().split()))
    kumi.append(k)
    score.append(s)


question_num = int(input())




first_cumsum=[0]*(n+1)
second_cumsum=[0]*(n+1)

#累積和の計算
for i in range(n):   # nは任意の番号
    if kumi[i]==1:
        first_cumsum[i+1]=first_cumsum[i]+score[i]
        second_cumsum[i+1]=second_cumsum[i]

    else:
        first_cumsum[i+1]=first_cumsum[i]
        second_cumsum[i+1]=second_cumsum[i]+score[i]

for j in range(question_num):
    array=list(map(int,input().split()))
    #print(array)

    first_kazu=array[0]
    end_kazu=array[1]

    first_wa=0
    second_wa=0

    first_wa=first_cumsum[end_kazu]-first_cumsum[first_kazu-1]
    second_wa=second_cumsum[end_kazu]-second_cumsum[first_kazu-1]

print(first_wa,second_wa)

