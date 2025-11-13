# 両方1しか考慮できていない

H, W = map(int, input().split())





if H==W==1:

    print(1)

    exit()



light_H = (H+1)//2

light_W = (W+1)//2



print(int(light_H*light_W))
