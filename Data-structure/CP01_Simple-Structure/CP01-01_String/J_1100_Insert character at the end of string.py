"""
1100: 문자열 끝에 문자 삽입

문제 설명
알파벳 대소문자로 구성된 문자열 A가 주어진다. 문자열 A의 길이가 k가 될 때까지 
문자열 A의 마지막 문자를 문자열 A의 끝에 붙이는 삽입 동작을 반복 수행하자. 
입력으로 문자열 A가 주어질 때 삽입 동작을 반복 수행한 후 길이가 k인 문자열 A를 출력하자.

입력 설명
첫 번째 줄에 문자열 A가 주어진다.
두 번째 줄에 정수 k가 주어진다.

제한 사항 :
- 3 ≤ 문자열 A 길이 ≤ 1,000
- 문자열 A 길이 ≤ k ≤ 10,000
- 파이썬에서 문자열 A를 입력받을때 input().strip() 함수를 사용해야 함. (이유: 문자열의 끝에 있는 개행문자를 제거하기 위함)

출력 설명
첫 번째 줄에 삽입 동작을 반복 수행한 후 길이가 k인 문자열 A를 출력한다.

입력 예시 복사
abcde
7

출력 예시 복사
abcdeee

"""
# 1) 반복문
S = input().strip()
k = int(input())

def solution(S, k):
    while True:
        S += S[-1]
        if len(S)==k:
            break
    return S
    
print(solution(S, k))


# 2) 반복문 X
S = input().strip()
k = int(input())

def solution(S, k):
    return S + S[-1]*(k-len(S))

print(solution(S, k))


# code ref: joonlab(1100) / 알고리즘 분류: 문자열, 구현