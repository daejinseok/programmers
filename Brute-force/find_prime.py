from itertools import permutations

def solution(numbers):

    nl = list(map(int, numbers))
    nm = []

    for i in range(1, len(nl) + 1):
        nm = nm + list(permutations(nl, i))

    print(nm)
    print(len(nm))




solution("1234567")