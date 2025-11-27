n,m=map(int,input().split())
hen_list=[]
hen_dic={}
for i in range(m):
    hen_list+=list(map(int,input().split()))
    if hen_list[2*i]>hen_list[2*i+1]:
        if hen_list[2*i] not in hen_dic.keys():
            hen_dic[hen_list[2*i]]=[hen_list[2*i+1]]
        else:
            hen_dic.pop(hen_list[2*i])
    else:
        if hen_list[2*i+1] not in hen_dic.keys():
            hen_dic[hen_list[2*i+1]]=[hen_list[2*i]]
        else:
            hen_dic.pop(hen_list[2*i+1])

print(len(hen_dic.keys()))