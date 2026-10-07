class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        ans = []

        def dfs(i, target, curr):

            if target == 0:
                ans.append(curr.copy())
                return

            if i == len(candidates) or target < 0:
                return

            curr.append(candidates[i])
            dfs(i, target - candidates[i], curr)
            curr.pop()

            dfs(i + 1, target, curr)

        dfs(0, target, [])

        return ans