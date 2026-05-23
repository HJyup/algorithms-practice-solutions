class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # bruteforce -> O(n^2) just check every possible container
        low, high = 0, len(heights) - 1
        ans = 0

        while low < high:
            ans = max(ans, (high - low) * min(heights[high], heights[low]))

            if heights[high] <= heights[low]:
                high -= 1
            else:
                low += 1

        return ans
        