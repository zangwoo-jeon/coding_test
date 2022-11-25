import heapq

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]
array.sort()

# 맨 처음 시작하는 강의의 종료 시간을 room 에 저장
room = []
heapq.heappush(room, array[0][1])

for i in range(1, n):
    # 만약 현재 강의의 시작시간이 맨 처음 시작하는 강의의 종료시간보다 빠르면 방 추가
    if array[i][0] < room[0]:
        heapq.heappush(room, array[i][1])
    # 현재 강의의 시작 시간이 맨 처음 시작하는 강의의 종료시간보다 느리면 맨 앞 강의를 빼고 이 강의 추가
    else:
        heapq.heappop(room)
        heapq.heappush(room, array[i][1])

print(len(room))
