from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기 상어의 좌표와 사이즈
x, y, size = 0, 0, 2

# 현재 그래프 위치 삽입
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j

def bfs(x, y, shark_size):
    # 방문 여부
    visit = [[0]*n for _ in range(n)]
    # 거리
    distance = [[0]*n for _ in range(n)]
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1
    # 먹을 수 있는 물고기의 거리 밑 좌표 삽입할 리스트
    temp = []
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                # 아기 상어의 사이즈보다 작거나 같으면 이동 가능
                if graph[nx][ny] <= shark_size:
                    Q.append((nx, ny))
                    visit[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                # 아기 상어보다 작은 물고기가 있으면 temp에 삽입
                if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                    temp.append((nx, ny, distance[x][y] + 1))
    # 나중에 pop으로 끝에를 뽑아낼 거여서 거리가 먼것부터 가까운 것으로 설정
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))

# 먹은 먹이 수
count = 0
# 분 수
result = 0
while True:
    # 먹을 수 있는 먹이 수 저장
    shark = bfs(x, y, size)
    # 먹을 수 있는 물고기 없으면 탈출
    if len(shark) == 0:
        break
    # 먹을 수 있는 먹이의 좌표 밑 거리
    nx, ny, dist = shark.pop()
    # 분수를 저장
    result += dist
    # 현재 좌표와 먹이를 먹은 좌표 0
    graph[x][y], graph[nx][ny] = 0, 0
    # 먹이를 먹은 좌표에서 다시 시작
    x, y = nx, ny
    # 먹은 먹이 수 증가
    count += 1
    # 먹은 먹이가 현재 사이즈와 같으면 사이즈 증가
    if count == size:
        size += 1
        count = 0
print(result)
