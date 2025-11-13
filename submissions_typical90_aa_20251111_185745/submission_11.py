# 計算量とinputの文字表示でWA
user_num = int(input("Enter the number of users: "))

user_list = []

for i in range(user_num):

    user = input("Enter user name: ")

    if user not in user_list:

        user_list.append(user)

        print(i+1)
