# 二分探索ロジックエラー

import math

list=[]

N=int(input())

for i in range(N):

    list+=[input()]



def binary(s):

    left=0

    right=len(check)

    if(right==0):return -1

    while(True):

        key=math.floor((left+right)/2)

        # print(left, key, right)



        if(check[key]==s):

            return key

        elif(check[key]>s):

            right=key

        else:

            left=key



        if(right-left<=1):

            return -1





def binary_right(s):

    left=-1

    right=len(check)

    while(True):

        key=int((left+right)/2)

        # print(left, key, right)

        if(right-left<=1):

            if left==-1:

                return -1

            return key

        if(check[key]>s):

            right=key

        else:

            left=key





check=["b", "c", "f", "h"]



for i in range(N):

    if  binary(list[i]) == -1:

        print(i+1)

        check.insert(binary_right(list[i])+1, list[i])



# print(binary_right("a"))

# print(binary_right("d"))

# print(binary_right("e"))

# print(binary_right("f"))

# print(binary_right("i"))



