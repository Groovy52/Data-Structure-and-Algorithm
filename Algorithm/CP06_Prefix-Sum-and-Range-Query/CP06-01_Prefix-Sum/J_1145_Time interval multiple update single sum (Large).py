# 1145: 시간 구간 다중 업데이트 단일 합 (Large)

# 틀린 코드
n = int(input())
A = list()
for _ in range(n):
    a, b, c = input().split()
    A.append((a, b, c))

def strtotime(timestr):
    h = int(timestr[:2])
    m = int(timestr[3:5])
    s = int(timestr[6:])

    return h*60*60 + m*60 + s

"""
# B[i]는 시간 구간 i-1부터 i 구간의 값을 저장

B 길이는 86400
인덱스는 0 ~ 86399까지 가능
"""
B = [0]*24*60*60
for t, s, e in A:
    st = strtotime(s)
    et = strtotime(e)
    if t=='1':
        B[st] += 1
        """
        문제 조건에서 종료 시각 h2:m2:s2는 최대 23:59:59까지 가능
        이 시간을 초로 바꾸면:
            23*3600 + 59*60 + 59 = 86399
            즉, et = 86399가 될 수 있음.
        """
        B[et+1] -= 1
        """
        B[86400] -= 1이 되는데, B[86400]은 존재하지 않음.
        """
        """
        B[st] += 1
        B[et + 1] -= 1 => 이건 끝점을 포함하는 [st, et] 구간에 더할 때 자주 쓰는 방식
        h1:m1:s1 ~ h2:m2:s2는 사실상 초 인덱스로 보면 [st, et) 구간으로 봐야 함.
        """
    else:
        for i in range(len(B)-1):
            B[i+1] += B[i]
        print(sum(B[st:et]))

# 잘못된 개념 고친 코드
n = int(input())
A = list()
for _ in range(n):
    a, b, c = input().split()
    A.append((a, b, c))

def strtotime(timestr):
    h = int(timestr[:2])
    m = int(timestr[3:5])
    s = int(timestr[6:8])

    return h*60*60 + m*60 + s

B = [0]*24*60*60 # B[t] = t초 ~ (t+1)초
for n, s, e in A:
    st = strtotime(s)
    et = strtotime(e)
    if n=='1':
        B[st] += 1
        B[et] -= 1
    else:
        for i in range(len(B)-1):
            B[i+1] += B[i]
            
        print(sum(B[st:et])) # B[t] = t초 ~ (t+1)초


# code ref: joonlab(1145) / 알고리즘 분류: 누적합