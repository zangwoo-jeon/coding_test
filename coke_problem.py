a, b, n = map(int, input().split())

def solution(a, b, n):
    result = 0

    while n >= a:
        count = 0
        now = b*(n//a)
        result += now
        count += n % a
        n = now
        n += count
        print("못 마신 병 수 : ", count)
        print("이번에 받은 병 수 : ", now)
        print("총 받은 병 수 : ", result)
        print("현재 병 수", n)


    return result

print(solution(a, b, n))
