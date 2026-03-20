# 1118: 정수 합을 재귀로 


# 잘못된 코드
import sys 

sys.setrecursionlimit(10**6)

n = int(input())

def solution(n, ans):
    ans += n
    while n > 0: # while n > 0 안에서 n이 절대 바뀌지 않아서, 0이 될 일이 없음!!
        """
        안쪽은 안쪽대로 n-1로 내려가서 0까지 가다가, 
        안쪽 호출이 끝나고 돌아와도, 바깥 호출의 n은 여전히 5임
        왜냐면 바깥에서 n을 n -= 1 같은 걸로 줄인 적이 없기 때문.
        
        """
        
        solution(n-1, ans)
    return ans 

solution(n, 0)


# 올바른 코드 1) ans를 사용해 누적값을 인자로 들고 재귀로 내려가는 방식
import sys 

sys.setrecursionlimit(10**6)

n = int(input())

def solution(n, ans):
    if n == 0:
        return ans 
    return solution(n-1, ans+n)

solution(n, 0)


# 올바른 코드 2) return 값으로 합 쌓는 방식
import sys 

sys.setrecursionlimit(10**6)

n = int(input())

def solution(n):
    if n == 0:
        return 0 
    return n + solution(n-1)

solution(n)



# code ref: joonlab(1118) / 알고리즘 분류: 완전탐색, 구현, 재귀