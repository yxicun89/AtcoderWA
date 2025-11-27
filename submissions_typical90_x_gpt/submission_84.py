# 入力
N , K = map( int , input().split() )
A = list( map( int , input().split() ))
B = list( map( int , input().split() ))
#print(N,K,A,B)

# 最低限必要な操作回数を求める
cnt = 0
for i in range(N):
    cnt += abs( A[i] - B[i] )
if (K-cnt)%2 == 0:
    print("Yes")
else:
    print("No")