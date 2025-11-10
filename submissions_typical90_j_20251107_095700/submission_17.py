# Sample input data based on the example
N = 7
student_data = [
    (1, 72),
    (2, 78),
    (2, 94),
    (1, 23),
    (2, 89),
    (1, 40),
    (1, 75)
]
Q = 1
queries = [
    (2, 6)
]

# Prepare prefix sums for class 1 and class 2
prefix_class1 = [0] * (N + 1)
prefix_class2 = [0] * (N + 1)

for i in range(1, N + 1):
    c, p = student_data[i - 1]
    prefix_class1[i] = prefix_class1[i - 1] + (p if c == 1 else 0)
    prefix_class2[i] = prefix_class2[i - 1] + (p if c == 2 else 0)

# Process each query and print results
for l, r in queries:
    sum_class1 = prefix_class1[r] - prefix_class1[l - 1]
    sum_class2 = prefix_class2[r] - prefix_class2[l - 1]
    print(sum_class1, sum_class2)

