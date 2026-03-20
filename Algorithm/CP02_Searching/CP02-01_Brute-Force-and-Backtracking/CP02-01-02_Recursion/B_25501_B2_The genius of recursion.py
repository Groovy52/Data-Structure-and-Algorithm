# 25501: 재귀의 귀재

str_list = []
N = int(input().strip())
for _ in range(N):
    str_list.append(input())

def recursion(A, s, e):
    global call
    call += 1
    
    if s >= e:
        return 1 
    elif A[s] != A[e]:
        return 0
    return recursion(A, s+1, e-1)

def isPalindrom(A):
    return recursion(A, 0, len(A)-1)

for str_ in str_list:
    global call
    call = 0

    print(isPalindrom(str_), call)


# code ref: backjoon(25501) / 알고리즘 분류: 구현, 문자열, 재귀