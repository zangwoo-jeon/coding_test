import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if visit[x][y] != -1:
        return visit[x][y]

    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[x][y] > graph[nx][ny]:
            ways += dfs(nx, ny)

    visit[x][y] = ways
    return visit[x][y]

print(dfs(0, 0))
