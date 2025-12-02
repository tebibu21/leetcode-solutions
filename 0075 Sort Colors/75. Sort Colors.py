class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        r, w, b = counts
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:b+r+w] = [2] * b

