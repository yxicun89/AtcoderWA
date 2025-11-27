N = int(input())
user_name = []
count = 1

for _ in range(N):
  reg_name = str(input())
  if reg_name not in user_name:
    print(count)
    count = count+1
    user_name.append(reg_name)
