n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

start = []
link = []

result = float("Inf")

def dfs(index):
    global result
    # start 리스트에 절반이 들어가면 시작
    if index == n // 2:
        # start 와 link 팀의 합 0으로 초기화
        startSum = 0
        linkSum = 0
        # link팀에 start팀의 멤버를 제외한 인원을 넣기
        for i in range(0, n):
            if i not in start:
                link.append(i)
        # 0번째 멤버부터 차례대로 넣었을 때의 팀의 총합 계산
        for i in range(0, n//2 - 1):
            for j in range(i+1, n // 2):
                startSum += graph[start[i]][start[j]] + graph[start[j]][start[i]]
                linkSum += graph[link[i]][link[j]] + graph[link[j]][link[i]]
        # start 팀과 link 팀의 차이
        diff = abs(startSum - linkSum)
        # 차이가 이전 값들보다 작으면
        if result > diff:
            # 현재 값으로 저장
            result = diff
        # link 팀 초기화
        link.clear()
        return

    for i in range(n):
        # 해당 멤버 i가 스타트 팀에 들어가있으면 넘어감
        if i in start:
            continue
        # 해당 멤버가 이전에 스타트 팀에 들어간 적 있으면 넘어감
        if len(start) > 0 and start[len(start) - 1] > i:
            continue
        start.append(i)
        dfs(index + 1)
        start.pop()

dfs(0)
print(result)