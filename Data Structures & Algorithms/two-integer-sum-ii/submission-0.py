class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            resolved_target = numbers[l] + numbers[r]

            if resolved_target == target:
                return [l+1, r+1]

            if resolved_target < target:
                l += 1
            else:
                r -= 1

        return []
        