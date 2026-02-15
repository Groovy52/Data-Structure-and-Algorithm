"""
1107: 문자열 정렬하기

알파벳 소문자로 구성된 문자열 A가 주어진다. 문자열 A에는 중복된 문자가 존재할 수 있다.
문자열 A에 있는 모든 문자를 오름차순으로 정렬한 문자열 B를 출력하자. 
예를 들어, 문자열 A = 'cab'인 경우 A에 있는 문자 'c', 'a', 'b'를 오름차순 정렬한 문자열 B는 'abc'가 된다.
"""

A = input().strip()

def solution(A):
    return ''.join(sorted(A))
    
print(solution(A))



# code ref: joonlab(1107) / 알고리즘 분류: 문자열, 구현