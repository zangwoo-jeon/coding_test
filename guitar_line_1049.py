n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

graph.sort()
six_min = graph[0][0]

for i in range(len(graph)):
    graph[i][0], graph[i][1] = graph[i][1], graph[i][0]

graph.sort()
one_min = graph[0][0]

if six_min <= one_min*6:
    result = six_min*(n//6) + min(six_min, one_min*(n%6))
else:
    result = one_min*n

print(result)