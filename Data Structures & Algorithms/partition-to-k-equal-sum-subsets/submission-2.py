class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 1. Preprocess (prunning based on values)
        # 2. How u wanna compare it?

        # Backtrack
        # 1. Base condition
        # 2. For loop
        # 3. Check condition
        # 4. Backtrack ->
        # 5. Remove prev idea

        # NOTE! For backtracking problems, whne you go to next deep level you need to assume
        # that previous level was done correctly

        # Try to solve the problem to a single condition.
        # Example. instead finding the target and then divide. Division into subparts is already
        # problem for the backtracking so tartget should deducable from the inputs
        n = len(nums)
        sm = sum(nums)

        if sm % k != 0:
            return False

        need = sm // k
        partitions = [0] * k

        if nums[0] > need:
            return False

        nums.sort(reverse=True)

        def backtrack(i: int) -> bool:
            # assume that all previous subsets were formed.
            if i == n:
                return True

            for j in range(len(partitions)):
                if partitions[j] + nums[i] <= need:
                    partitions[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    partitions[j] -= nums[i]

                if partitions[j] == 0:
                    break

            return False

        return backtrack(0)

        