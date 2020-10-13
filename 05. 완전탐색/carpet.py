# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

import math

def y_iter(n):
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 :
            yield (int(n/i), i)

def solution(brown, yellow):

    for y in y_iter(yellow):
        col = y[0]
        row = y[1]
        if brown == (col+row+2)*2:
            return [col+2, row+2]

    return []


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.09ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.09ms, 10.2MB)
# 테스트 8 〉	통과 (0.11ms, 10.1MB)
# 테스트 9 〉	통과 (0.09ms, 10.2MB)
# 테스트 10 〉	통과 (0.13ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)