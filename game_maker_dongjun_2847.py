n = int(input())
array = []

for _ in range(n):
    a = int(input())
    array.append(a)

result = 0

# 맨 끝에서 부터 맨 앞까지 
for i in range(n-1, 0, -1):
    # 만약 현재보다 이전값이 더 크거나 같으면 뺴야하는 값을 저장하고 이전값은 현재값 -1 로 저장
    if array[i] <= array[i-1]:
        result += array[i-1] - array[i] + 1
        array[i-1] = array[i] - 1

print(result)
