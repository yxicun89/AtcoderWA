from bisect import bisect_left, bisect_right

n = int(input())
s_n = [input() for _ in range(n)]

registered_users = []
for i in range(n):
    if bisect_left(registered_users, s_n[i]) == bisect_right(registered_users, s_n[i]):
        registered_users.append(s_n[i])
        print(i + 1)
