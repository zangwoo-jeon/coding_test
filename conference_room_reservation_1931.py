n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

array.sort(key=lambda x:(x[1], x[0]))

count = 1
end_time = array[0][1]

for i in range(1, n):
    if array[i][0] >= end_time:
        count += 1
        end_time = array[i][1]

print(count)
