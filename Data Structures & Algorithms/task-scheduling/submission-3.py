import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        time = 0
        queue = deque([])

        heap = []
        for count in freq.values():
            heapq.heappush(heap, -count)

        while heap or queue:
            time += 1

            if queue and queue[0][0] == time:
                _, count = queue.popleft()
                heapq.heappush(heap, count)

            if heap:
                processed = heapq.heappop(heap) + 1
                if processed < 0:
                    queue.append((time + n + 1, processed))

        return time