# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
import math

def is_prime(n):
    # set에서 미리 0,1 는 빼버림
    # if n < 2:
    #     return 0
    if n % 2 == 0 and n > 2: 
        return 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return 0
    return 1

def solution(numbers):

    char_list = list(numbers)
    num_set = set()

    for i in range(1, len(char_list) + 1):
        num_set |= set(map(int, map(''.join, (permutations(char_list, i)))))    

    # is_prime 향상을 위해 0,1은 미리 뺌    
    num_set -= set(range(0, 2))

    return sum(map(is_prime, num_set))

def p(n):
    print(n, solution(n))

p('17')
p('011')

# 테스트 1 〉	통과 (0.07ms, 10.4MB)
# 테스트 2 〉	통과 (2.08ms, 10.5MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.85ms, 10.4MB)
# 테스트 5 〉	통과 (3.48ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.07ms, 10.4MB)
# 테스트 8 〉	통과 (3.45ms, 10.4MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (3.69ms, 10.4MB)
# 테스트 11 〉	통과 (0.59ms, 10.4MB)
# 테스트 12 〉	통과 (0.22ms, 10.4MB)