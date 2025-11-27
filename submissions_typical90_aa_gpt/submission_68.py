
N = int(input())

name = set()#set()は集合を表しており、重複を許さないため、リストよりも計算量が低い

for day in range(1,N):

    S = input()

    if S not in name:

        name.add(S)

        print(day)
