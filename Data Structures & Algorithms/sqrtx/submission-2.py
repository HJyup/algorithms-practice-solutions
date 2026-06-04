class Solution:
    def mySqrt(self, x: int) -> int:
        # lies between 0 and x
        left , right = 0, x

        while left <= right:
            mid = (left + right) // 2
            val = mid * mid

            if val == x:
                return mid
            elif val > x:
                right = mid - 1
            else:
                left = mid + 1

        return right