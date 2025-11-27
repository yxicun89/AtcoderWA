q = int(input())



top = []

bottom = []

query = []



for i in range(q):

    a = list(map(int, input().split()))

    if a[0] == 1:

        top.append({"id" : i, "num" : a[1]})

    elif a[0] == 2:

        bottom.append({"id" : i, "num" : a[1]})

    else:

        query.append({"id" : i, "num" : a[1]})



top.reverse()

all_list = top + bottom



start = 0

for i in range(len(all_list)):

    if all_list[i]["id"] == 1:

        start = i

        break



for i in query:

    for j in range(start, -1, -1):

        if all_list[j]["id"] < i["id"]:

            start = j

        else:

            break

    print(all_list[start + i["num"] - 1]["num"])

