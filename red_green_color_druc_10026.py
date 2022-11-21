from collections import deque
from copy import deepcopy

n = int(input())

graph = [list(map(str, input())) for _ in range(n)]
sak_graph = deepcopy(graph)

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            sak_graph[i][j] = "R"
visit = [[0]*n for _ in range(n)]
n_visit = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph, visit):

    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                Q.append((nx, ny))
    return True

result_f, result_s = 0, 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and bfs(i, j, graph, visit) == True:
            result_f += 1
        if n_visit[i][j] == 0 and bfs(i, j, sak_graph, n_visit) == True:
            result_s += 1

print(result_f, result_s)
