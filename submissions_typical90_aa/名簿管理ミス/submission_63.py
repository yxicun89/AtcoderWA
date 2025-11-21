# for文の範囲がおかしい

n = int(input())

s = [input() for _ in range(n)]

si = [i for i in range(n,-1,-1)]

ans = [-1] * n

sorteds = sorted(s,reverse=True)



ssi = dict(zip(sorteds,si))



rssi = sorted(ssi.items(),key=lambda x:x[1])



for i in rssi:

    print(i[1])
