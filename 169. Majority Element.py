from typing import List


def majorityElement(nums: List[int]) -> int:
    from collections import defaultdict

    numDict = defaultdict(int)

    for num in nums:
        numDict[num] += 1 

    return sorted(numDict, key=numDict.__getitem__, reverse=True)[0]

nums = [3,2,3]
nums = [2,2,1,1,1,2,2]

print(majorityElement(nums))