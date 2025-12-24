class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_num = 1
        r_num = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i - 1
            l_arr[i] = l_num
            r_arr[j] = r_num
            l_num *= nums[i]
            r_num *= nums[j]

        return [l*r for l, r in zip(l_arr, r_arr)]    
    