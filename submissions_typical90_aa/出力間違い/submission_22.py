N =int(input())
name=[]
for i in range (N):
    in_name =input()
    hit=False
    for n in name:
        if(in_name==n):
            hit=True
            break
    if(hit==False):
        print(i)
        name.append(in_name)
