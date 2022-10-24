n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
result = 0

def dfs(x, y):
    global result
    graph[x][y] = 0
    result += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:

            dfs(nx, ny)
    return result

count = 0
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(dfs(i, j))
            result = 0
            count += 1

answer.sort()
print(count)
for i in answer:
    print(i)