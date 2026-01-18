"""
1103: 연속된 문자 A 제거

문제 설명
알파벳 대소문자로 구성된 문자열 S가 주어진다. 문자열 S에서 문자 ‘a’ 또는 ‘A’가 
두 번 이상 연속된 부분 문자열을 하나의 문자 ‘a’로 치환한 문자열을 문자열 T라고 하자. 문자 ‘a’와 ‘A’가 혼합되어 연속으로 나타나는 부분 문자열도 하나의 문자 ‘a’로 치환한다. 입력으로 문자열 S가 주어지면, 문자열 S를 치환한 문자열 T를 출력하자.

참고로, 아래 도움에 입력 예시 2가 추가 되었다.

입력 설명
첫 번째 줄에 문자열 S가 주어진다.
제한 사항 :
- 3 ≤ 문자열 S 길이 ≤ 1,000

출력 설명
첫 번째 줄에 문자열 T를 출력한다.

입력 예시 
ABAaaAAAaab

출력 예시
ABab

[입력]
ABAAa

[출력]
ABa

"""
# 1) 
S = input().strip()

def solution(S):
    T = ''
    for s in S:
        """
        아래 조건의 반대:
        s=='a' or s=='A' (s가 a거나 A면)
        """
        if s!='a' and s!='A':
            T += s 
        else:
            if T[-1:]!='a' and T[-1:]!='A':
                T += s 
            else:
                T = T[:-1] + 'a'
    return T
    
print(solution(S))


# 2) 
S = input().strip()

def solution(S):
    T = ''
    i = 0 
    while i < len(S):
        if S[i] != 'a' and S[i] != 'A':
            T += S[i]
            i += 1
            continue
        
        j = i + 1 
        while j < len(S):
            if S[j] != 'a' and S[j] != 'A':
                break
            j += 1
        
        if j - i == 1:
            T += S[i]
        else:
            T += S[i].lower()
            
        i = j 
        
    return T

print(solution(S))


# code ref: joonlab(1103) / 알고리즘 분류: 문자열, 구현