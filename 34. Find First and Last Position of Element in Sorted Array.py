from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            firstIndex = nums.index(target)
        except Exception:
            return [-1, -1]
        
        onlyNums = []
        [onlyNums.append(num) for num in nums if num == target]
        targets = len(onlyNums)
        if targets > 1:
            return [firstIndex, firstIndex + targets - 1]
        else:
            return [firstIndex, firstIndex]