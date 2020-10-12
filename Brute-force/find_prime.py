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


print(solution("17"))