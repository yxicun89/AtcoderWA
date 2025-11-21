n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

add_a = 0
add_b = 0

for i in a:
    add_a += i
for i in b:
    add_b += i

if abs(add_a-add_b) == k or abs(add_a-add_b) > k and abs(add_a-add_b)%2 == k%2:
    print("Yes")
else:
    print("No")