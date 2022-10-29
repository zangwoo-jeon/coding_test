T = int(input())

def dfs(v):
    global count
    visit[v] = 1
    for i in range(n):
        if visit[i] == 0 and graph[v][i] == 1:
            count += 1
            dfs(i)

for _ in range(T):
    n, m = map(int, input().split())
    visit = [0]*n
    graph = [[0]*n for _ in range(n)]
    result = 1001
    count = 0
    for i in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = graph[b-1][a-1] = 1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i)
                result = min(result, count)
    print(result)