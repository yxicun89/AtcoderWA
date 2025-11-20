# import math
# from collections import defaultdict

# n, k = map(str, input().split())
# for _ in range(int(k)):
#     result = 0
#     n = n[::-1]
#     for i in range(len(n)):
#         result += int(n[i]) * 8 ** i
#     to_9_result = ""
#     while result > 0:
#         to_9 = result % 9
#         if to_9 == 8:
#             to_9 = 5
#         result //= 9
#         to_9_result = str(to_9) + to_9_result
#     n = to_9_result
# print(n)

n, k = map(str, input().split())
k = int(k)

for _ in range(k):
    result = 0
    n = n[::-1]  # 逆順にするのは一度だけで良い
    for i in range(len(n)):
        result += int(n[i]) * 8 ** i  # 文字列の各桁を整数に変換して計算
    to_9_result = ""
    while result > 0:
        to_9 = result % 9
        if to_9 == 8:
            to_9 = 5
        to_9_result = str(to_9) + to_9_result
        result //= 9
    n = to_9_result  # 新しいnとして更新
print(n)