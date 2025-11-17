from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first() -> int:
            l, r = 0, len(nums) - 1
            first = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    first = m
                    r = m - 1  # continue left
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return first

        def find_last() -> int:
            l, r = 0, len(nums) - 1
            last = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    last = m
                    l = m + 1  # continue right
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return last

        return [find_first(), find_last()]
