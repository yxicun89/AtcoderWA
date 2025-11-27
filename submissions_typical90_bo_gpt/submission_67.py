# 10進数からn進数へ
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

n,k=map(int,input().split())
n=str(n)
for _ in range(k):
    n_8=int(n,8)
    n_9=Base_10_to_n(n_8,9)
    new_n=[]
    for ele in str(n_9):
        if ele=="8":
            new_n.append("5")
        else:
            new_n.append(ele)
    n="".join(new_n)

print(n)

