from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        from collections import defaultdict

        intDict = defaultdict(int)

        sortedNums = sorted(nums)
        
        for num in sortedNums:
            intDict[f"{num}"] += 1
            if intDict[f"{num}"] >= 2:
                return True
        return False