# 9935: 문자열 폭발

# 틀린 코드
"""
틀린 원인: 문제를 잘못 이해함

아래 코드는 "폭발 문자열에 포함된 문자 자체를 전부 제거"하고 있는데,
문제는 "폭발 문자열과 정확히 연속해서 일치하는 부분 문자열만 제거"해야 함.
    => 그 이유는 문제에서 "문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.

    새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다." 라고 언급했기 때문
예를 들어, 문자열 mirkovC4nizCC44, 폭발 문자열: C4라면
1) mirkovC4nizCC44 => mirkov"C4"nizCC44 => mirkovnizCC44
2) mirkovnizC"C4"4 => mirkovnizC4
3) mirkovniz"C4" => mirkovniz
"""
S = input()
F = input()

stack = []
for s in S:
    if s not in list(F):
        stack.append(s)
print(''.join(stack) if stack else 'FRULA')


# 
stack = []
flen = len(F)
for ch in S:
    stack.append(ch)
    if len(stack) >= flen and ''.join(stack[-flen:])==F:
        for _ in range(flen):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')


# code ref: backjoon(9935) / 알고리즘 분류: 자료구조, 문자열, 스택