class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        sm = sum(nums)

        if sm % k != 0:
            return False

        target = sm // k
        subsets = [0] * k

        if max(nums) > target:
            return False

        nums.sort(reverse = True)

        def backtrack(i: int) -> None:
            if i == n:
                return True

            for j, subset in enumerate(subsets):
                if j > 0 and subsets[j] == subsets[j - 1]:
                    break
                    
                if subset + nums[i] <= target:
                    subsets[j] += nums[i]
                    if backtrack(i + 1):
                        return True

                    subsets[j] -= nums[i]

            return False

        return backtrack(0)