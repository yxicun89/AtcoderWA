def input_easy():
  N = int(input())
  List_N = []
  for val in range(N):
    List_N.append(list(map(int,input().split())))
  Q = int(input())
  List_Q = []
  for val in range(Q):
    List_Q.append(list(map(int,input().split())))
  return List_N,List_Q
  
def Sum_Score(pre_List):
  List_N = pre_List[0]
  List_Q = pre_List[1]
  Sum_1 = [0]
  Sum_2 = [0]
  for i in range(1,len(List_N)+1):
    if List_N[i-1][0]==1:
      Sum_1.append(Sum_1[i-1]+List_N[i-1][1])
      Sum_2.append(Sum_2[i-1])
    else:
      Sum_1.append(Sum_1[i-1])
      Sum_2.append(Sum_2[i-1]+List_N[i-1][1])
  for val in List_Q:
    Ans_1 = Sum_1[val[1]]-Sum_1[val[0]-1]
    Ans_2 = Sum_2[val[1]]-Sum_2[val[0]-1]
    print(' '.join(map(str,[Ans_1,Ans_2])))