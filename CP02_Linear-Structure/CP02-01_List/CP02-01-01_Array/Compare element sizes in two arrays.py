"""
# 1073: 두 배열 원소 크기 비교
n개의 정수가 저장된 배열 A와 B가 주어진다. 
배열 A의 원소는 a0, a1, ..., an-1이다. 배열 B의 원소는 b0, b1, ..., bn-1이다. 
i=0,1,2,.., n-1에 대하여 배열 A의 원소 ai와 배열 B의 원소 bi를 차례대로 비교한다. 
이렇게 비교한 결과 ai가 bi보다 더 큰 i의 개수를 a, bi가 ai보다 
더 큰 i의 개수를 b라고 하자. ai와 bi가 같은 경우는 a,b에 영향을 주지 않음에 주의하자. 
a가 b보다 더 크면 1을, 그렇지 않으면 0을 출력하자.
"""

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solution(a, b):
    ans_a = 0
    ans_b = 0
    for ai, bi in zip(a, b):   
        if ai > bi:
            ans_a +=1
        elif ai < bi:
            ans_b += 1 
            
    return int(ans_a > ans_b)

print(solution(a, b))


# code ref: joonlab(1073)
