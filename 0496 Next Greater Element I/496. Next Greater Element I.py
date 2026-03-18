from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # find next greater for nums2
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # remaining elements have no greater
        for num in stack:
            next_greater[num] = -1

        # build answer for nums1
        return [next_greater[num] for num in nums1]