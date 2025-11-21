n, p, q = map(int, input().split())
A = list(map(int, input().split()))
A_res = [0]*len(A)
for idx, a in enumerate(A):
  A_res[idx] = a % p
# A_ele = list(set(A_res))
# A_ele_num = [0]*len(A_ele)
cnt = 0

# for a_res in A_res:
#   for a_idx, a_ele in ennumerate(A_ele):
#     if a_res == a_ele:
#       A_ele_num[a_idx]++
      
idx_list = []
all_idx = len(A_res)
for idx1 in range(0, all_idx-4):
  for idx2 in range(idx1+1, all_idx-3):
    for idx3 in range(idx2+1, all_idx-2):
      for idx4 in range(idx3+1, all_idx-1):
        for idx5 in range(idx4+1, all_idx):
          if A_res[idx1] * A_res[idx2] * A_res[idx3] * A_res[idx4] * A_res[idx5] == q:
            # idx_list.append([idx1, idx2, idx3, idx4, idx5])
            cnt += 1
            
# idx_set = set(map(tuple, idx_list))

print(cnt)