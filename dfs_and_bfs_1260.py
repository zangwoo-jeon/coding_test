from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visit_bfs = [0]*(n+1)
visit_dfs = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    Q = deque()
    Q.append(v)
    visit_bfs[v] = 1
    while Q:
        v = Q.popleft()
        print(v, end=" ")
        for i in range(n+1):
            if visit_bfs[i] == 0 and graph[v][i] == 1:
                visit_bfs[i] = 1
                Q.append(i)

def dfs(v):
    print(v, end=" ")
    visit_dfs[v] = 1
    for i in range(n+1):
        if visit_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

dfs(v)
print()
bfs(v)
