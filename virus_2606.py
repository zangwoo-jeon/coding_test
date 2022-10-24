n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

result = 0

def dfs(v):
    global result
    visit[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and visit[i] == 0:
            result += 1
            dfs(i)

dfs(1)
print(result)
