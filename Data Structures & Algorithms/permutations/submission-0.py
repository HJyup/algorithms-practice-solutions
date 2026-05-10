class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(permutation, st):
            if len(st) == len(nums):
                self.res.append(permutation)
                return

            for num in nums:
                if num not in st:
                    st.add(num)
                    dfs(permutation + [num], st)
                    st.remove(num) 

        dfs([], set())
        return self.res
        