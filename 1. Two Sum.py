class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        indexes = []
        for i, num in enumerate(nums):
            h[num] = i

        for i, num in enumerate(nums):
            desired = target - num 
            if desired in h and h[desired] != i:
                return i, h[desired]