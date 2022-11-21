m, n = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = max(array)
result = 0

while start <= end:
    mid = (start+end)//2
    # 애들한테 줄수 있는 과자 갯수
    total = 0
    # 공평하게 줄수가 없으면 0출력
    if mid == 0:
        break
    # total에 애들한테 줄 수 있는 총 과자 갯수 넣기
    for i in array:
        if i >= mid:
            total += (i//mid)
    # 줄 수 있는 과자 수가 애들 수보다 많으면 해당수를 저장하고 start를 중간값다음으로 옮겨서 주는 량을 늘림
    if total >= m:
        result = mid
        start = mid + 1
    # 받을 수 있는 인원수가 적으면 end를 중간값전으로 옮겨서 주는 량을 줄임
    else:
        end = mid - 1

print(result)
