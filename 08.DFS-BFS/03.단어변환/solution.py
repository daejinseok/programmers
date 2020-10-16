import doctest

# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3


def is_one_diff(a, b):
    """
    >>> is_one_diff('abc', 'abc')
    False
    >>> is_one_diff('bbc', 'abc')
    True
    >>> is_one_diff('bbb', 'abc')
    False
    """
    diff = False

    for i in range(len(a)):
        if a[i] != b[i]:
            if diff:
                return False
            diff = True

    return diff


def solution(begin, target, words):
    answer = 0
    return answer


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))

doctest.testmod()