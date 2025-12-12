class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(32):  # 0 to 31 for 32-bit integers
            bit_sum = 0
            for num in nums:
                # Mask the i-th bit and count
                if (num >> i) & 1:
                    bit_sum += 1
            if bit_sum % 3 != 0:
                # Set the i-th bit in the result
                result |= (1 << i)

        # Handle negative numbers (32-bit signed integer logic)
        if result >= 2 ** 31:
            result -= 2 ** 32

        return result