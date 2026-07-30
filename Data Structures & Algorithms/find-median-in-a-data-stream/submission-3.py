import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num) # append always to the left

        if self.right and -self.left[0] > self.right[0]:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
            heapq.heappush(self.left, -heapq.heappop(self.right))

        if len(self.left) - len(self.right) > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float: # O(1)
        print(self.left, self.right)
        length = len(self.left) + len(self.right)

        if length == 0:
            return 0

        if length % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2

        return -self.left[0]