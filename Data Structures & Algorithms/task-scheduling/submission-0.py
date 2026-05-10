from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        time = 0

        for task in tasks:
            counter[task] += 1

        heap = [-count for count in counter.values()]
        heapq.heapify(heap)

        queue = deque()
        while heap or queue:
            time += 1

            if heap:
                task = -heapq.heappop(heap)
                task -= 1

                if task > 0:
                    queue.append((time + n, -task))

            while queue and queue[0][0] <= time:
                heapq.heappush(heap, queue.popleft()[1])

        return time
        
