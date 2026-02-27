# 1115: 조건에 맞는 정수의 개수 (Small1

# 1) 260227
n = int(input())

def solution(n):
    max_num = 10**n 
    min_num = 10**(n-1)
    whole_range = range(min_num, max_num)
    if n==1:
        return list(whole_range)
    else:
        answer = []
        for i in whole_range:
            str_num = str(i)
            if '0' in str_num:
                continue
            else:
                ok = True
                for j in range(n-1):
                    diff = abs(int(str_num[j+1])-int(str_num[j]))
                    if diff > 2:
                        ok = False
                if ok:
                    answer.append(i)

        return answer

print(len(solution(n)))

# 2) 260227
def solution(n):
    answer = 0
    for A in range(10**(n-1), 10**n):
        if is_ok(A):
            answer += 1
    return answer

def is_ok(A):
    r = A % 10
    A //= 10
    while A > 0:
        h = A % 10
        A //= 10
        if abs(h-r) > 2 or r==0:
            return False
        r = h
    return True

# 3) 2)보다 더 정확함 (문제의도에 맞음: 처음부터 자릿수의 0 유무 확인하기)
# 2) 260227
def solution(n):
    answer = 0
    for A in range(10**(n-1), 10**n):
        if is_ok(A):
            answer += 1
    return answer

def is_ok(A):
    r = A % 10
    A //= 10
    if r==0:
        return False
    while A > 0:
        h = A % 10
        A //= 10
        if abs(h-r) > 2 or h==0:
            return False
        r = h
    return True


# code ref: joonlab(1115) / 알고리즘 분류: 구현, 완전탐색, 대학