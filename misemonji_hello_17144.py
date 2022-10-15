
r, c, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1

for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i+1
        break

def spread():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    tmp_arr = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        tmp_arr[nx][ny] += graph[i][j] // 5
                        tmp += graph[i][j] // 5
                graph[i][j] -= tmp
    for i in range(r):
        for j in range(c):
            graph[i][j] += tmp_arr[i][j]

def air_up():
    #    오, 위, 왼, 아
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny
'''
def air_up():
    # 첫 열 아래
    for i in range(up):
        graph[i+1][0] = graph[i][0]
    # 첫 행 왼쪽
    graph[0][0:c-1] = graph[0][1:c]
    for i in range(up):
        graph[i][c-1] = graph[i+1][c-1]
    graph[up][2:c] = graph[up][1:c-1]
    graph[up][1] = 0
    graph[up][0] = -1

def air_down():
    for i in range(down, r-1):
        graph[i][0] = graph[i+1][0]
    graph[r-1][0:c-1] = graph[r-1][1:c]
    for i in range(r-1, down, -1):
        graph[i][c-1] = graph[i-1][c-1]
    graph[down][2:c] = graph[down][1:c-1]
    graph[down][0] = -1
    graph[down][1] = 0
'''
for i in range(t):
    spread()
    air_up()
    air_down()

result = 0
for i in range(r):
    result += sum(graph[i])
result += 2
print(result)
