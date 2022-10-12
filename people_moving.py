n, l, r = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    # 해당 위치 방문 처리
    visit[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 있고 아직 방문하지 않았으면서 해당 조건 안에 범위 안에 있으면
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                # 해당 위치 저장하고 dfs
                loca.append((nx, ny))
                dfs(nx, ny)
    # 해당 위치값들 리턴
    return loca

count = 0

while True:
    visit = [[0]*n for _ in range(n)]
    # 종료 조건
    flag = False
    for i in range(n):
        for j in range(n):
            loca = [(i, j)]
            # 아직 방문하지 않은 위치들 실행
            if visit[i][j] == 0:
                loca = dfs(i, j)
            # 해당 위치들의 값이 1이면 조건 만족 x 1 이상이면 실행
            if len(loca) > 1:
                flag = True
                sum = 0
                # loca의 값들에 해당하는 그래프의 값을 sum에 추가
                for x, y in loca:
                    sum += graph[x][y]
                # 평균값 구함
                avg = sum // len(loca)
                # 해당 값으로 변경
                for a, b in loca:
                    graph[a][b] = int(avg)
    # 더이상 국경을 열 수 없으면 break
    if flag == False:
        print(count)
        break
    # 아직 국경을 열 수 있으면 카운트 증가
    count += 1