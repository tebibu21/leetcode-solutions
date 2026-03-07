class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        total = 0
        for num in nums:
            total += num
            res.append(total)
        return res