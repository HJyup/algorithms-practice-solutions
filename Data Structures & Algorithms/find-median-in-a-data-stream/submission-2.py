import heapq

class MedianFinder:

    def __init__(self):
        self.first = [] # Max-heap
        self.second = [] # Min-heap
        self.size = 0

    def _getSize(self) -> int:
        return len(self.first) + len(self.second)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first, -num)

        # Move largest value from first to second and then check do we need to do changes
        to_move = -heapq.heappop(self.first)
        heapq.heappush(self.second, to_move)

        if len(self.second) > len(self.first):
            to_move = heapq.heappop(self.second)
            heapq.heappush(self.first, -to_move)

        return None
        

    def findMedian(self) -> float:
        size = self._getSize()
        
        if size % 2 == 0:
            return (-self.first[0] + self.second[0]) / 2
            
        else:
            return -self.first[0]

        return -1

# The first value goes to first
# push to the first
# if difference from first to second > 1: value from first goes to second
# if last element of first bigger than first element in second -> move to second
# if second bigger than first -> move element form second to first