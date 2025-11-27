n = int(input())

#name_list = []
#for i in range(n):
#    s = input()
#    if not s in name_list:
#        name_list.append(s)
#        print(i+1)

#name_list = [[] for i in range(15)]
#for i in range(n):
#    s = input()
#    if not s in name_list[len(s) - 1]:
#        name_list[len(s) - 1].append(s)
#        print(i + 1)

name_set = set()
for i in range(n):
    s = input()
    if s in name_set:
        continue
    name_set.add(s)
    print(i - 1)
