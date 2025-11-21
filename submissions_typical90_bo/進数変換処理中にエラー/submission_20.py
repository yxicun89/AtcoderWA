# 9進数変換処理抜け

N, K = map(int, input().split())

for i in range(K):

    tmp = 0

    N_str = str(N)

    N_str_inv = N_str[::-1]

    for j in range(len(N_str_inv)):

        tmp += pow(8, j)*int(N_str_inv[j])

    tmp = int(str(tmp).replace("8", "5"))

    N = tmp

print(N)
