class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []

        def dfs(start: int, current_sum: int):
            if current_sum == target:
                res.append(list(comb))
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                val = candidates[i]
                # pruning: if val makes sum exceed target, break (candidates sorted)
                if current_sum + val > target:
                    break
                comb.append(val)
                # allow repeating same candidate -> pass i (not i+1)
                dfs(i, current_sum + val)
                comb.pop()

        dfs(0, 0)
        return res