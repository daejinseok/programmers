# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return 0
    if n % 2 == 0 and n > 2: 
        return 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return 0
    return 1

def solution(numbers):

    char_list = list(numbers)
    char_perm = []

    for i in range(1, len(char_list) + 1):
        char_perm = char_perm + list(permutations(char_list, i))

    num_set = set(map(lambda n : int(''.join(n)), char_perm))
    return sum(map(is_prime, num_set))


print(solution('17'))
print(solution('011'))


# 테스트 1 〉	통과 (0.08ms, 10.3MB)
# 테스트 2 〉	통과 (2.53ms, 10.6MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (1.39ms, 10.5MB)
# 테스트 5 〉	통과 (7.46ms, 11.5MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.09ms, 10.4MB)
# 테스트 8 〉	통과 (6.70ms, 11.5MB)
# 테스트 9 〉	통과 (0.06ms, 10.3MB)
# 테스트 10 〉	통과 (4.24ms, 10.5MB)
# 테스트 11 〉	통과 (0.63ms, 10.5MB)
# 테스트 12 〉	통과 (0.29ms, 10.4MB)