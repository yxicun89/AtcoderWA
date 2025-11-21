N, M = map(int, input().split())
List = []
for i in range(M):
    ab_list = list(map(int, input().split()))
    List.append(ab_list)

num_ = 0
for k in range(1, N+1):
    num = 0
    for l in range(M):
        if k in List[l]:
            if sum(List[l])<2*k:
                num =+1
    if num == 1:
        num_ = +1
print(num_)

