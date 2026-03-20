"""
1089: 학생 이름 찾기

문제 설명
n개의 학생 이름이 공백으로 구분된 문자열 A가 주어진다. 문자열 A에는 중복된 학생 이름이 존재하지 않는다. 
m개의 학생 이름이 공백으로 구분된 문자열 B가 주어진다. 문자열 B에는 중복된 학생 이름이 존재할 수 있다. 
하나의 학생 이름은 알파벳 소문자로 이루어져 있다.

문자열 A에 포함된 학생 이름 중에서 문자열 B에 존재하지 않는 학생 이름을 오름차순으로 출력하자. 
문자열 A에 포함된 학생 이름 중에서 문자열 B에 존재하지 않는 학생 이름이 1개 이상 존재하는 입력만 주어진다.

입력 설명
첫 번째 줄에 문자열 A가 주어진다.
두 번째 줄에 문자열 B가 주어진다.

출력 설명
문자열 A에 저장된 학생 이름 중에서 문자열 B에 존재하지 않는 학생 이름을 오름차순으로 출력한다. 한 줄에 하나의 학생 이름을 출력한다.

입력 예시 복사
aaa bbb ccc ddd eee fff
aaa ddd ddd aaa eee

출력 예시 복사
bbb
ccc
fff
"""

A = input().split()
B = input().split()

def solution(A, B):
    bdict = dict()
    for b in B:
        if not b in bdict:
            bdict[b] = 1
        else:
            bdict[b] += 1
            
    answer = []
    for a in A:
        if not a in bdict:
            answer.append(a)
    answer.sort()
    return answer

for ans in solution(A, B):
    print(ans)


# code ref: 딕셔너리, 맵, 문자열, 구현, 정렬