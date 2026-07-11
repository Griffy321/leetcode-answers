from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        # print(merged)
        length = len(merged)
        if length % 2 == 1:
            return merged[length//2]
        else:
            index1 = length//2 - 1
            index2 = length//2
            return (merged[index1] + merged[index2]) / 2