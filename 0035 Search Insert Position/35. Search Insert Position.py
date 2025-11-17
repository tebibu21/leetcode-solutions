from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Return the index if target is found.
        If not found, return the index where it would be inserted in order.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # left is the insertion point when the loop ends
        return left
