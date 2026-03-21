"""
1090: 비슷한 전화번호 표시

문제 설명
n개의 전화번호가 공백으로 구분된 문자열 A가 주어진다. 문자열 A에는 중복된 전화번호가 존재할 수 있다. 추가로, 하나의 전화번호 
가 주어진다. 전화번호는 문자 '1' ~ 문자 '9'로 이루어진 문자열이다. 
문자열 A에 포함된 전화번호 중에서 전화번호 B와 다르면서 B를 접두사로 갖는 전화번호의 개수를 출력하자. 
전화번호 T의 접두사는 T의 첫 번째 문자부터 한 개 이상의 연속된 문자로 구성된 부분 문자열을 의미한다. 
예를 들어, 전화번호 T="1234"의 접두사는 전화번호 "1", "12", "123", "1234"이다.

입력 설명
첫 번째 줄에 문자열 A가 주어진다.
두 번째 줄에 전화번호 B가 주어진다.

출력 설명
문자열 A에 포함된 전화번호 중에서 전화번호 B와 다르면서
B를 접두사로 갖는 전화번호의 개수를 출력한다.

전화번호는 문자 '1' ~ 문자 '9'로 이루어진 문자열이다.

입력 예시 복사
12 121 123 1234 134 135 21 2134
12

출력 예시 복사
3
"""

# 1) 잘못된 코드
A = input().split()
B = input().strip()

def solution(s, T):
    vdict = dict()
    for num in s:
        vdict[num] = [num[:i] for i in range(len(num))]
    print(vdict)
    ans = 0
    for k, v in vdict.items():
        if T in v: 
            ans += 1
    return ans 

print(solution(A, B))

# 2) 
A = input().split()
B = input().strip()

freq = dict()
for num in A:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

ans = 0
for num, cnt in freq.items():
    if num != B and num.startswith(B):
        ans += cnt  

print(ans)

# 3) 모든 테케 확인해보기!!!
A = input().split()
B = input().strip()

def solution(A, B):
    D = {}
    for number in A:
        for i in range(len(number)-1):
            num = number[:i+1]
            if num in D:
                D[num] += 1
            else:
                D[num] = 1 
    if B in D:
        return D[B]
    else:
        return 0

print(solution(A, B))


# code ref: joonlab(1090) / backjoon(26041) / 알고리즘 분류: 딕셔너리, 맵, 문자열, 구현