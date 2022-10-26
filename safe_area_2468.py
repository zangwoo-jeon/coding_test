import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

maximum = 0

for i in graph:
    for j in i:
        maximum = max(maximum, j)

def dfs(x, y, value):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > value and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, value)


result = 0
for k in range(maximum):
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visit[i][j] == 0:
                dfs(i, j, k)
                cnt += 1
    result = max(result, cnt)

print(result)