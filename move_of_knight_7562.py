from collections import deque

T = int(input())

def dfs(x, y, obx, oby):
    if x == obx and y == oby:
        return 0

    Q = deque()
    Q.append((x, y))
    dx = [-1, -2, 1, 2, -2, -1, 1, 2]
    dy = [-2, -1, -2, -1, 1, 2, 2, 1]
    while Q:
        x, y = Q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                Q.append((nx, ny))
    return graph[obx][oby]

for _ in range(T):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(dfs(a, b, c, d))
