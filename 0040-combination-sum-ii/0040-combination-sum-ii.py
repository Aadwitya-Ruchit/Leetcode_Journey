class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()
        ans = []

        def dfs(i, target, curr):

            if target == 0:
                ans.append(curr.copy())
                return

            if i == len(candidates) or target < 0:
                return

            curr.append(candidates[i])
            dfs(i + 1, target - candidates[i], curr)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, target, curr)

        dfs(0, target, [])
        return ans