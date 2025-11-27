N, M =map(int,input().split())

hen_dict = {str(i+1):0 for i in range(N)}

for i in range(M):
    a, b = map(int, input().split())
    if a < b:
        b=str(b)
        hen_dict[b] += 1

    else:
        a = str(a)
        hen_dict[a] += 1

keys = [k for k, v in hen_dict.items() if v == 1]
print(" ".join(keys))