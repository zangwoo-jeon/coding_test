from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
sea = []

for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
           sea.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    Q = deque(sea)
    melt = []

    while Q:
        for _ in range(len(Q)):
            x, y = Q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    melt.append((1, x, y))

        for _ in range(len(melt)):
            ice, x, y = melt.pop()
            graph[x][y] -= ice
            if graph[x][y] < 0:
                graph[x][y] = 0

def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                return False
    return True

def count_island(x, y):
    Q = deque()
    Q.append((x, y))

    if graph[x][y] == 0 or visit[x][y] == 1:
        return False
    visit[x][y] = 1

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] > 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                Q.append((nx, ny))

    return True

result = 0
while True:
    if check() == True:
        print(0)
        break

    count = 0
    visit = [[0] * m for _ in range(n)]
    bfs()
    result += 1

    for i in range(n):
        for j in range(m):
            if count_island(i, j) == True:
                count += 1

    if count >= 2:
        print(result)
        break


