# インデックス出力エラー

import time



N = int(input())



S_list = []

for i in range(N):

    S_list.append([i, input()])



S_list = sorted(S_list, reverse=False, key= lambda x: (x[1], x[0]))



prev_S = ''

for i in range(N):

    if prev_S != S_list[i][1]:

        print(i+1)

    prev_S = S_list[i][1]



#print(S_list)



s_time = time.time()



#print(time.time() - s_time)

