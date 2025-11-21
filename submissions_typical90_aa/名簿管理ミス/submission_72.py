# namesetにデータ加えてない

n = int(input())



nameset = set()



check = []

for i in range(n):

    name = input()

    if not name in nameset:

        check.append(i)



for i in check:

    print(i+1)
