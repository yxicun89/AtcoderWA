N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#2+1+2nならいける。

#まずは各要素についての差を求める
diff = sum(list(map(lambda a,b: abs(a-b) , A,B)))

n = K-diff
if n%2 ==0:
    print("Yes")
else:
    print("No")