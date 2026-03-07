from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = set()
        for x in arr:
            # Build new subarray ORs ending at current element
            nxt = {x} | {x | y for y in cur}
            ans |= nxt         # Add to total results
            cur = nxt          # Move forward

        return len(ans)
