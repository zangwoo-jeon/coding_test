n = int(input())
graph = []

for i in range(n):
    name, day, month, year = input().split()
    day, month, year = int(day), int(month), int(year)
    graph.append([name, day, month, year])

graph.sort(key=lambda x:(x[3], x[2], x[1]))

print(graph[n-1][0])
print(graph[0][0])
