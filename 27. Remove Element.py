from typing import List


def removeElement(nums: List[int], val: int) -> int:

    new = []

    for index in range(len(nums)):
        if nums[index] != val:
            new.append(nums[index])

    nums[::] = new

    return len(nums)

# nums = [3,2,2,3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))