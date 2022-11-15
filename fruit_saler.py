K, M = map(int, input().split())
Score = list(map(int, input().split()))

def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        result = []
        for i in range(-1, -m-1, -1):
            result.append(score.pop())
        answer += m*min(result)
    return answer

print(solution(K, M, Score))
