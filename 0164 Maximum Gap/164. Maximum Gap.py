from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        mn, mx = min(nums), max(nums)

        if mn == mx:
            return 0

        n = len(nums)
        gap = math.ceil((mx - mn) / (n - 1))

        bucket_min = [float("inf")] * (n - 1)
        bucket_max = [float("-inf")] * (n - 1)

        # put numbers into buckets
        for num in nums:
            if num == mn or num == mx:
                continue

            idx = (num - mn) // gap
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)

        max_gap = 0
        prev = mn

        for i in range(n - 1):
            if bucket_min[i] == float("inf"):
                continue

            max_gap = max(max_gap, bucket_min[i] - prev)
            prev = bucket_max[i]

        max_gap = max(max_gap, mx - prev)

        return max_gap