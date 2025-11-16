class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Width is distance between pointers
            width = right - left
            # Height is the smaller of two vertical lines
            h = min(height[left], height[right])
            max_area = max(max_area, h * width)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# --- quick tests ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([4,3,2,1,4], 16),
        ([1,2,1], 2)
    ]

    for heights, expected in tests:
        result = sol.maxArea(heights)
        print(f"{heights} -> {result}  (expected {expected})")