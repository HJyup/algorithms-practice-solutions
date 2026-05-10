import heapq

class MedianFinder:

    def __init__(self):
        self.first = [] # Max-heap
        self.second = [] # Min-heap
        self.size = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first, -num)

        if len(self.first) - len(self.second) > 1:
            to_move = -1 * heapq.heappop(self.first)
            heapq.heappush(self.second, to_move)

        if self.first and self.second and -self.first[0] > self.second[0]:
            to_move = -1 * heapq.heappop(self.first)
            heapq.heappush(self.second, to_move)

        if len(self.second) > len(self.first):
            to_move = heapq.heappop(self.second)
            heapq.heappush(self.first, -to_move)

        self.size += 1
        

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            first = -self.first[0]
            second = self.second[0]

            return (first + second) / 2

        else:
            return -self.first[0]

# The first value goes to first
# push to the first
# if difference from first to second > 1: value from first goes to second
# if last element of first bigger than first element in second -> move to second
# if second bigger than first -> move element form second to first