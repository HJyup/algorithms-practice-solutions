class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sm = sum(nums)
        n = len(nums)

        if sm % k != 0:
            return False

        target = sm // k # what we wanna achieve for each division pile
        used = set() # used letter for partition
        
        nums.sort(reverse=True) # try largest values first
        if nums[0] > target: # number cannot get any partition
            return False

        def dfs(i: int, curr: int) -> bool:
            if i == k:
                return True

            prev = None
            for j in range(n):
                if j not in used:
                    new_curr = curr + nums[j]
                    if new_curr > target:
                        continue

                    if prev and prev == nums[j]:
                        continue

                    used.add(j)
                    prev = nums[j]
                    if new_curr == target:
                        if dfs(i + 1, 0):
                            return True

                    elif dfs(i, new_curr):
                        return True

                    used.remove(j)

            return False

        return dfs(1, 0)