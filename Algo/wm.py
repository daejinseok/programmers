def solution(n):
    return ('수박'*(n//2+n%2))[0:n]

def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

def solution2(n):
    return ('수박'*n)[0:n]

for i in range(1, 10):
    #print(10/2)
    #print(10//2)
    print(solution(i))
    print(solution2(i))
    #print(water_melon(i))