name_list=[]

N = int(input())

for i in range(N):
    Si = input()
    if Si in name_list:
        continue
    elif not Si in name_list:
        name_list.append(Si)
        print(i)
         