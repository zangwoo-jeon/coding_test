from collections import deque

# 오른쪽 확인
def check_right(start, direction):
    # 제일 오른쪽 바퀴가 아니거나 현재 바퀴의 2번째 칸과 다음 바퀴의 6번째 칸이 같으면 시마이
    if start >= 4 or tobni[start][2] == tobni[start+1][6]:
        return
    # 현재 바퀴의 2번째 칸과 오른쪽 바퀴의 6번째 칸의 극이 다르면 다음 오른쪽 바퀴 체크
    if tobni[start][2] != tobni[start+1][6]:
        check_right(start+1, -direction)
        # 오른쪽 바퀴 반대 방향으로 돌림
        tobni[start+1].rotate(-direction)

def check_left(start, direction):
    if start <= 1 or tobni[start-1][2] == tobni[start][6]:
        return

    if tobni[start-1][2] != tobni[start][6]:
        check_left(start-1, -direction)
        tobni[start-1].rotate(-direction)

tobni = {}

for i in range(1,5):
    tobni[i] = deque(list(map(int, input())))

k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    # 오른쪽 바퀴 확인
    check_right(a, b)
    # 왼쪽 바퀴 확인
    check_left(a, b)
    # 현재 바퀴 회전
    tobni[a].rotate(b)

result = 0
for i in range(4):
    result += 2**i*tobni[i+1][0]

print(result)