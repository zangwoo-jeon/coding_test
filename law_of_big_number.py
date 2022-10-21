n, m, k = map(int, input().split())

graph = list(map(int, input().split()))

graph.sort(reverse=True)
first = graph[0]
second = graph[1]

result = (first*k + second)*(m//(k+1)) + first*(m % (k+1))

print(result)

