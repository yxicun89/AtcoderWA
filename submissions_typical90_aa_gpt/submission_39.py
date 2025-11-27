N = int(input())

user = []
day = []
for i in range(N):
    register = input()
    if register not in user:
        day.append(i)
    user.append(register)

for i in range(len(day)):
    print(day[i])