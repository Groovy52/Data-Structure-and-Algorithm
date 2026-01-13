"""
# 중복된 원소 제거
"""

nums = [0,0,0,1,2,2,2]

# (1)
def solution(nums):
    if len(nums) == 0:
        return 0
    
    curr = []
    curr.append(nums[0])
    for n in nums[1:]:
        if curr[-1] == n:
            continue 
        else:
            curr.append(n)
        
    return len(curr)


# (2)
from typing import List 

def solution(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0 

    curr = nums[0]
    cnt = 1 
    for i in range(1, len(nums)):
        if nums[i] != curr:
            curr = nums[i]
            cnt += 1 
    
    return cnt
    

# code ref: 쓰면서 익히는 알고리즘과 자료구조/Array/1.4 정렬된 배열에서 중복 제거