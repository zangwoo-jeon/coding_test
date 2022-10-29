r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = set()
ans = 0
def dfs(x, y, count):
    global ans
    if ans < count:
        ans = count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not graph[nx][ny] in result:
            result.add(graph[nx][ny])
            dfs(nx, ny, count+1)
            result.remove(graph[nx][ny])

result.add(graph[0][0])
dfs(0, 0, 1)
print(ans)