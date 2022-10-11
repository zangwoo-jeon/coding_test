n, m = map(int, input().split())
graph = []
r, c, d = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))
#     북  동  남  서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 최종 결과값
result = 0

def dfs(x, y, direc):
    global result
    # 청소 안되있으면
    if graph[x][y] == 0:
        graph[x][y] = 2
        result += 1
    # 모든 방향에 대해서
    for _ in range(4):
        # 왼쪽방향으로 턴
        nd = (direc + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        # 그 방향이 청소 안되있으면
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            dfs(nx, ny, nd)
            return
        direc = nd
    # 모든 방향이 청소가 되있으면 후진
    nd = (direc + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    # 후진 했는데 벽이면 시마이
    if graph[nx][ny] == 1:
        return
    # 벽 아니면 후진한 뒤에 재시작
    dfs(nx, ny, direc)

dfs(r, c, d)
print(result)
