class Solution:
    def subsets(self, nums):
        res = []       # Final answer will go here
        sol = []       # Temporary list to build each subset

        def backtrack(i):
            # Base case: If we finished the list
            if i == len(nums):
                res.append(sol[:])   # Add a copy of current subset
                return

            # Choice 1: Don’t take nums[i]
            backtrack(i + 1)

            # Choice 2: Take nums[i]
            sol.append(nums[i])      # Add it to current subset
            backtrack(i + 1)
            sol.pop()                # Remove it to try other paths

        backtrack(0)    # Start from index 0
        return res