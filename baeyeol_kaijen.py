from itertools import permutations
from copy import deepcopy

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
rcs = [list(map(int, input().split())) for _ in range(k)]

ans = 100*m + 1

for p in permutations(rcs, k):
    copy_graph = deepcopy(graph)

    for r, c, s in p:
        r -= 1
        c -= 1
        for i in range(s, 0, -1):
            # 맨 위 맨 오른쪽 값 저장
            tmp = copy_graph[r-i][c+i]
            # ->
            copy_graph[r-i][c-i+1:c+i+1] = copy_graph[r-i][c-i:c+i]
            # 위로 전진
            for row in range(r-i, r+i):
                copy_graph[row][c-i] = copy_graph[row+1][c-i]
            # <-
            copy_graph[r+i][c-i:c+i] = copy_graph[r+i][c-i+1:c+i+1]
            # 아래로 전진
            for row in range(r+i, r-i, -1):
                copy_graph[row][c+i] = copy_graph[row-1][c+i]
            # 맨 오른쪽 맨위 바로 아래줄
            copy_graph[r-i+1][c+i] = tmp
    # 최소값 계산
    for row in copy_graph:
        ans = min(ans, sum(row))

print(ans)

