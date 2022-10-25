from collections import deque

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    count = 0

    def bfs(x, y):
        Q = deque()
        Q.append((x, y))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        if graph[x][y] == 0:
            return False

        while Q:
            x, y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    Q.append((nx, ny))

        return True

    for i in range(n):
        for j in range(m):
            if bfs(i, j) == True:
                count += 1

    print(count)