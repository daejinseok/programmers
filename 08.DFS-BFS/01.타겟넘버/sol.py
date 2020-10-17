# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3


count = 0
nums = []
num_len = 0
t = 0

def s(sumv, idx, b):

    global count, nums, num_len, t

    #print(sumv, idx, b)

    val = b and nums[idx] or -nums[idx]
    sumv = sumv + val

    if idx == num_len:
        if sumv == t:
            count = count + 1
        return
    
    s(sumv, idx+1, True)
    s(sumv, idx+1, False)


def solution(numbers, target):

    global nums, num_len, t
    nums = numbers
    num_len = len(nums) - 1
    t = target

    s(0, 0, True)
    s(0, 0, False)

    return count

print(solution([1, 1, 1, 1, 1], 3))


# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (330.69ms, 10.2MB)
# 테스트 2 〉	통과 (331.42ms, 10.3MB)
# 테스트 3 〉	통과 (0.57ms, 10.3MB)
# 테스트 4 〉	통과 (1.82ms, 10.3MB)
# 테스트 5 〉	통과 (11.21ms, 10.1MB)
# 테스트 6 〉	통과 (1.12ms, 10.3MB)
# 테스트 7 〉	통과 (0.60ms, 10.2MB)
# 테스트 8 〉	통과 (3.33ms, 10.3MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0