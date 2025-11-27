n, k = map(int, input().split())

lst1 = list(map(int, input().split()))

lst2 = list(map(int, input().split()))

total = 0



for item1, item2 in zip(lst1, lst2):

    total += abs(item1 - item2)



print('Yes' if total < k and k % 2 == total % 2 else 'No')

