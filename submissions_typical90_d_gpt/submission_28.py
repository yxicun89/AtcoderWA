import copy

H, W = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(H)]

transpose_lst = [list(x) for x in zip(*lst)]

new_lst = copy.deepcopy(lst)


for i in range(H):

  for j in range(W):

    t = sum(transpose_lst[j])

    new_lst[i][j] = sum(lst[i]) + t - lst[i][j]

print(new_lst)
