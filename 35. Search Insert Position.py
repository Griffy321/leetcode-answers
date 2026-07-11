class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            index = nums.index(target)
            return index
        elif target > nums[-1]:
            return len(nums)

        currentIndex = 0
        lastNum = 0
        while currentIndex < len(nums):
            # print(nums[currentIndex])
            lastNum = nums[currentIndex]
            if target < lastNum:
                return currentIndex
            currentIndex += 1