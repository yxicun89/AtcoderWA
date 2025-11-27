
import itertools



N, P, Q = map(int, input().split())

A = list(map(int, input().split()))



times=1

counter=0

for combo in itertools.combinations(A, 5):

    for x  in combo:

        times = (times * (x%P))%P

    if times ==  Q:

        counter += 1

print(counter)
