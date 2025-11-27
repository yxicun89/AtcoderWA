N = int(input())
S = [] 
for i in range(N):
    S.append(input())

L = []
unique_set = set()  # Use a set for faster membership checks
for i in range(N):
    if S[i] not in unique_set:  # O(1) membership check
        L.append(S[i])
        unique_set.add(S[i])  # Add to the set
        print(i)