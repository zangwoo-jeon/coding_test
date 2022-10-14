from collections import deque
# n : 로봇을 놓을 수 있는 길이. k : 종료 조건인 0의 갯수
n, k = map(int, input().split())
# 컨베이어 벨트의 내구도
belt = deque(list(map(int, input().split())))
# 로봇이 놓여져 있는 칸
robot = deque([0]*n)
# 최종 단계 횟수
result = 0

while True:
    # 밸트 회전
    belt.rotate(1)
    # 로봇 회전
    robot.rotate(1)
    # 내리는 자리가 되면 로봇 뺌
    robot[-1] = 0
    # 로봇이 컨베이어 벨트에 있으면
    if sum(robot):
        # 내리는 자리 바로 전부터 올리는 위치까지
        for i in range(n-2, -1, -1):
            # 로봇이 있고 다음 자리에는 로봇이 없으며 다음 자리의 내구도가 있으면 실행
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        # 내리는 자리에 도착하면 로봇 제거
        robot[-1] = 0
    # 3단계 : 올리는 위치에 내구도가 1 이상이면 로봇을 올리고 벨트 내구도 1 깍음
    if belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    result += 1
    # 종료조건되면 탈출
    if belt.count(0) >= k:
        break

print(result)