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
    one_diff = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if one_diff:
                return False
            one_diff = True
    return one_diff

from queue import Queue
def solution(begin, target, words):
    """
    >>> solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
    4
    >>> solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'])
    0
    """

    if target not in words:
        return 0

    v = set()
    q = Queue()
    q.put((0, begin))

    while(q):
        d, w = q.get()
        print(d, w)

        if w == target:
            return d

        for w2 in words:
            if is_one_diff(w, w2):
                q.put((d+1, w2))
                words.remove(w2)
    return d



import doctest
doctest.testmod()

