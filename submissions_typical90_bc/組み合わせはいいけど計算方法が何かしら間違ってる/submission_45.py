# 055 -Select5(2)
import itertools
n, p, q = map(int, input().split())
a_list = list(map(int, input().split()))
total = 0
count = 0

for five in itertools.combinations(a_list, 5):
    total = sum(five)
    if total%p == q:
        count += 1
print(count)
