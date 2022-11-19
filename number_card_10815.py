import sys
sys.setrecursionlimit(10**6)

n = int(input())
sanguen_card = list(map(int, input().split()))
sanguen_card.sort()
m = int(input())
find = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in find:
    print(binary_search(sanguen_card, i, 0, n-1), end=" ")
