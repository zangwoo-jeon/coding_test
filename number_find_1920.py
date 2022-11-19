import sys
sys.setrecursionlimit(10**6)

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
find = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if array[mid] == target:
        return 1

    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    else:
        return binary_search(array, target, mid+1, end)

for i in find:
    print(binary_search(array, i, 0, n-1))
