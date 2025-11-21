def binary_search(array, target, lr):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] >= target and array[mid - 1] < target:
            if array[mid] == target and lr == "r":
                return mid + 1
            else:
                return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

n = int(input())
class1score = []
class2score = []
class1number = []
class2number = []
for i in range(n):
    c, p = input().split()
    if c == "1":
        class1score.append(int(p))
        class1number.append(i + 1)
    elif c == "2":
        class2score.append(int(p))
        class2number.append(i + 1)
q = int(input())
for i in range(q):
    l, r = input().split()
    l = int(l)
    r = int(r)
    class1l_index = binary_search(class1number, l, "l")
    class1r_index = binary_search(class1number, r, "r")
    class2l_index = binary_search(class2number, l, "l")
    class2r_index = binary_search(class2number, r, "r")
    class1total = 0
    class2total = 0
    if class1score == []:
        class1total = 0
    else:
        class1total = sum(class1score[class1l_index:class1r_index])
    if class2score == []:
        class2total = 0
    else:
        class2total = sum(class2score[class2l_index:class2r_index])
    print(class1total, class2total)