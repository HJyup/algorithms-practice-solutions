from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, q = [], deque()
        n = len(nums)

        # Each elements is accessed only twice (adding to the q) and removing using
        # step 1 or step 2: therefore the time complexity is O(2n) -> O(n)

        for i in range(n):
            # remove elements from the back if they smaller (we will never used them)
            # since new element is more recent + bigger
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # fix problem with indecies, remove elements from the top which are out of date
            while q and q[0] < i - (k - 1):
                q.popleft()

            if i - (k - 1) >= 0:
                ans.append(nums[q[0]])

        return ans