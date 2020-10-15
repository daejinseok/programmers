
# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

v = [] 
N = 0
count = 0
coms = []

def walk(i):
    #print(i, v)
    if ( v[i] != -1 ) :
        return False

    v[i] = count

    for j in range(N):
        if coms[i][j] == 1 :
            walk(j)

    return True


def solution(n, computers):

    global v, N, count, coms
    N = n
    coms = computers
    v = [-1] * n
    count = 0

    for i in range(n):
        if walk(i) :
            count = count + 1

    return count

print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))

