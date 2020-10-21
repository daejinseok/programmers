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

        if len(remain) == 0:
            return used

        here = used[len(used-1)][1]
        ft = find_ticket(here, remain):

        if len(ft) == 0:
            return None

        result = None

        for i in ft:
            used2 = set(used)
            used2.add(i)
            remain2 = set(remain)
            remain2.remove(i)
            result = _walk(used2, remain2) 
        



    def find_ticket(from_city, remain):
        ft = []
        for i in remain:
            if ts[i][0] == from_city:
                ft.push(i)
        return ft




    for i in range(N):
        used = set(i)
        left = set(range(N))
        left.remove(i)
        all = _walk(set(i), remain)

        if all != None :
            break
            
    return all

import doctest
doctest.testmod()