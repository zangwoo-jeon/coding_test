from collections import deque
from copy import deepcopy
n = int(input())

graph = [list(input()) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
sac_graph = deepcopy(graph)

for i in range(n):
    for j in range(n):
        if sac_graph[i][j] == "G":
            sac_graph[i][j] = "R"

def bfs(x, y, G):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and G[nx][ny] == G[x][y]:
                Q.append((nx, ny))
                visit[nx][ny] = 1
    return True

result = 0
sac_result = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and bfs(i, j, graph) == True:
            bfs(i, j, graph)
            result += 1
visit = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and bfs(i, j, sac_graph) == True:
            bfs(i, j, sac_graph)
            sac_result += 1

print(result)
print(sac_result)