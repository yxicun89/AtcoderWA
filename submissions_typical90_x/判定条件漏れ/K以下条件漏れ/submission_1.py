# 総和の条件漏れ

n, k = map(int,input().split())



s1 = list(map(int, input().split()))

s2 = list(map(int, input().split()))

s3 = [0]*n



for i in range(n):

  s3[i] = abs(s1[i]-s2[i])



if abs(sum(s3)-k) % 2 == 0:

  print("Yes")

else:

  print("No")
