"""
1109: 문자열 나열하기

문제 설명
알파벳 소문자로 구성된 문자열 A가 주어진다. 문자열 A에는 중복된 문자가 존재하지 않는다. 
문자열 A에 있는 모든 문자를 재배열하여 생성되는 모든 문자열 집합을 문자열 A에 대한 P(A)라고 하자. 예를 들어, 문자열 A = 'ab'에 대한 P(A) = {'ab', 'ba'}이다.
입력으로 문자열 A가 주어질 때 문자열 A의 P(A)를 오름차순으로 출력하시오.


입력 설명
첫 번째 줄에 문자열 A가 주어진다.


제한 사항 :
- 1 ≤ 문자열 A 길이 ≤ 7


출력 설명
문자열 A에 대한 P(A)를 오름차순으로 출력한다. 한 줄에 P(A)의 원소 1개를 출력한다.


입력 예시
abc

출력 예시
abc
acb
bac
bca
cab
cba

"""
s = input().strip()

def solution(s):
    from itertools import permutations

    for i in sorted(permutations(s)):
        print(''.join(i))
        
solution(s)


# code ref: joonlab(1109) / 알고리즘 분류: 문자열, 구현, 완전탐색


"""
P(A) 중에서 사전 순으로 k번째인 문자열을 출력하려면?
"""
s, k = input().split()

def solution(s):
    from itertools import permutations  
    n_str = ''.join(sorted(permutations(s))[int(k)-1])
    
    return n_str
        
print(solution(s))


# code ref: joonlab(1110) / 알고리즘 분류: 문자열, 구현, 완전탐색


"""
P(A) 중에서 어떤 문자열이 사전 순으로 몇번째인지 출력하려면?
"""
s, s2 = input().split()

def solution(s):
    from itertools import permutations  
    p = sorted(permutations(s))
    
    for i in range(len(p)):
        if ''.join(p[i])==s2:
            return i+1
            
        
print(solution(s))

# code ref: joonlab(1112) / 알고리즘 분류: 문자열, 구현, 완전탐색
