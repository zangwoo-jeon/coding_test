n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)

for i in range(n):
    array[i] = array[i] + i + 1

print(max(array) + 1)
