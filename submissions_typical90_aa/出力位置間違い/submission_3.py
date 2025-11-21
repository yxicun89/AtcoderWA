N = int(input())

Name = []
for i in range(N):
  S = input()
  flag = 1 # True
  if(i != 0):
    for j in range(len(Name)):
      if(Name[j] == S): # すでに登録されている場合
        flag = 0 # False
    
  if(flag == 1): # 未登録だった場合
    print(i)
    Name.append(S)
    
      