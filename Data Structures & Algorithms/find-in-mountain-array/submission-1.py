class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # kinda rotated array
        n = mountainArr.length()
        memo = {}

        def binary_search(left: int, right: int, isLeft: bool) -> int:
            while left <= right:
                mid = (left + right) // 2 

                value = memo[mid] if mid in memo else mountainArr.get(mid)
                memo[mid] = value

                if value == target:
                    return mid
                elif value < target:
                    if isLeft:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if isLeft:
                        right = mid - 1
                    else:
                        left = mid + 1

            return -1

        # Find pivot
        left, right = 1, n - 1
        pivot = 1

        while left <= right:
            mid = (left + right) // 2
            value = memo[mid] if mid in memo else mountainArr.get(mid)
            value_left = memo[mid - 1] if mid - 1 in memo else mountainArr.get(mid - 1)
            value_right = memo[mid + 1] if mid + 1 in memo else mountainArr.get(mid + 1)

            memo[mid] = value
            memo[mid - 1] = value_left
            memo[mid + 1] = value_right

            if value_left < value > value_right:
                pivot = mid
                break
            elif value_left > value:
                right = mid - 1
            else:
                left = mid + 1

        if target == memo[pivot]:
            return pivot

        left = binary_search(0, pivot - 1, True)
        if left != -1:
            return left

        return binary_search(pivot + 1, n - 1, False)