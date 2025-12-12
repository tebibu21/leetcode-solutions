class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1    
        for i in counter:
            if counter[i] > (len(nums)/2):
                return i
