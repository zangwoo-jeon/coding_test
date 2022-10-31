from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = []

def bfs(x, y):
    result = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q = deque()
    Q.append((x, y))
    graph[x][y] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                result += 1
                Q.append((nx, ny))
    answer.append(result)
    return True

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            if bfs(i, j) == True:
                count += 1
                
print(count)
if answer == []:
    print(0)
else:
    print(max(answer))