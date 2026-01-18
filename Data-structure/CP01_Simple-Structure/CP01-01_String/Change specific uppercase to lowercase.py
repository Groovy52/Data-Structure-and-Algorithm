"""
1082: 알파벳 대소문자로 구성된 문자열 A가 주어진다. 한 개 이상의 알파벳 대문자가 공백으로 구분된 문자 목록 B
가 주어진다. 문자 목록 B에는 중복된 대문자가 존재하지 않는다. 문자 목록 B에 존재하는 모든 대문자 b에 대하여, 문자열 A에 존재하는 대문자 b를 
대응하는 소문자로 치환한 문자열을 C라고 하자. 입력으로 문자열 A와 문자 목록 B가 주어지면 문자열 C를 출력하자.
"""


A = input() # ABabC
B = input() # A B D

# Ex. 1
def solution(A, B):
    ans = ''
    for a in A:
        if a in B.split():
            ans += a.lower()
        else:
            ans += a 
    return ans 

print(solution(A, B)) # ababC

# Ex. 2
def solution(A, B):
    for b in B.split():
        A = A.replace(b, b.lower())
    
    return A

print(solution(A, B)) # ababC


# code ref: joonlab(1082)