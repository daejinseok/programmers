# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164


def solution(tickets):
    """
    >>> solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']])
    ['ICN', 'JFK', 'HND', 'IAD']
    >>> solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']])
    ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']
    """

    ts = tickets.sort()
    N = len(len(ts))

    def _walk(used, remain):




    for i in range(N):
        used = set(i)
        remain = set(range(N))
        remain.remove(i)
        all = _walk(set(i), remain)

        if all != None :
            break
            
    return all





import doctest
doctest.testmod()