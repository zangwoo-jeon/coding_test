from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i , j

def bfs(x, y, shark_size):
    distance = [[0]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    temp = []
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] <= shark_size:
                    Q.append((nx, ny))
                    visit[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                    temp.append((nx, ny, distance[x][y] + 1))
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))

count = 0
result = 0
while True:
    shark = bfs(x, y, size)
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()
    result += dist

    graph[x][y], graph[nx][ny] = 0, 0
    x, y = nx, ny
    count += 1
    if count == size:
        size += 1
        count = 0
print(result)
