class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colours = [0, 0, 0]
        
        for num in nums:
            colours[num] += 1        # O(n)

        total_count = 0
        for i in range(len(colours)):
            for _ in range(colours[i]):
                nums[total_count] = i
                total_count += 1