class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def dfs(i: int) -> None:
            ans.append(curr[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j + 1)
                curr.pop()

            return None

        dfs(0)
        return ans