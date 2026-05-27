class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # a < b, prefering smaller elements (bisect left?)

        l, r = 0, len(arr) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        l, r = ans, ans + 1
        while r - l - 1 != k:
            if l < 0:
                r += 1
            elif r >= len(arr) or x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1

        return arr[l + 1 : r]
                
            
            