N = int(input())
set_ = set()

for i in range(N):
    s = input()
    if s in set_:
        continue
    set_.add(s)
    print(i)