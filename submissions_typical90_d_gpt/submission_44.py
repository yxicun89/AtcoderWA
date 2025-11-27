
height, width = map(int, input().split(" "))

arr = [list(map(int, input().split(" "))) for _ in range(height)]

row_colum_list = [sum(arr[row]) for row in range(height)]

colum_list = [sum([arr[row][colum] for row in range(height)]) for colum in range(width)]

resultarr = [

    [row_colum_list[row] + colum_list[colum] - arr[row][colum] for row in range(height)]

    for colum in range(width)

]

print("".join(map(str, [" ".join(map(str, item)) + "\n" for item in resultarr])))

