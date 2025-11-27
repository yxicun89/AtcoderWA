# def main():
n, m = map(int, input().split())

graph = [0] * n

# print(graph)
# count = 0
for i in range(m):
    a, b = map(int, input().split())
    i = max(a, b) - 1
    if graph[i] == None:
        graph[i] = True
    elif graph[i] == True:
        graph[i] == False
    else:
        pass

print(graph.count(True))