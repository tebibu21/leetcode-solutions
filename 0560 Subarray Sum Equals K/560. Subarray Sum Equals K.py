from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1  # Base case: empty subarray sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            sum_count[prefix_sum] += 1

        return count