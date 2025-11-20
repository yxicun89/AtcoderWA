N,M = map(int,input().split())
larger_number_list = []
for i in range(M):
    a,b = map(int,input().split())
    larger_number = max(a,b)
    larger_number_list.append(larger_number)
    larger_number_set = set(larger_number_list)
print(len(larger_number_set))
