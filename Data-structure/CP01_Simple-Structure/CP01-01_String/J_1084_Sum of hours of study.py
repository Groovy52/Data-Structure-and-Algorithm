"""
1084: 공부한 시간의 합

한 명의 학생이 n일 동안 공부한 시간 목록이 공백으로 구분된 문자열 A가 주어진다. 
하루 동안 공부한 시간은 시:분 형태의 문자열로 주어지고 시, 분 모두 길이가 2인 문자열이다. 
학생이 n일 동안 공부한 전체 시간을 시:분 형태의 문자열로 출력하자. 
시는 길이가 2이상인 문자열, 분은 길이가 2인 문자열로 출력하자.
"""

# Ex 1. 
A = list(map(str, input().split())) # 00:00 23:00 23:00 23:30 23:30 23:00

def solution(A):
    ans = ''
    h = sum([int(a[:2]) for a in A])
    m = sum([int(a[3:]) for a in A])
    
    if m >= 60:
        h += m//60
        m = m%60 
    
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    
    return ans + h + ':' + m
    
print(solution(A)) # 116:00


# Ex 2. 
A = list(input().split())

def h_to_m(s):
    return int(s[:2]) * 60 + int(s[3:])

def solution(A):
    total_t = 0 
    for t in map(h_to_m, A):
        total_t += t
    
    h = total_t // 60 
    m = total_t % 60 
    
    return '%02d:%02d'%(h, m)
    
print(solution(A)) # 116:00



# code ref: joonlab(1084) / 알고리즘 분류: 문자열, 구현