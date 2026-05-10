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

        cooldown = deque()
        while heap or cooldown:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt < 0:
                    cooldown.append((time + n, cnt))

            while cooldown and cooldown[0][0] <= time:
                _, c = cooldown.popleft()
                heapq.heappush(heap, c)

        return time
        
