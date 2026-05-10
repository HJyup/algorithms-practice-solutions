class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort to make possible to use greedy discard for intervals
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        intervals.sort()

        # Idea
        # Have a queue for intervals. when we take a new query and interval can possibly answer this query
        # take it and pop it to the heap
        # Heap will be working by the idea of fast answer to the questions. if we enounter top value that is
        # not part of the interval we can remove it
        res = [0] * len(queries)

        queue = collections.deque(queries)
        interval_queue, heap = collections.deque(intervals), []

        while queue:
            idx, query = queue.popleft()

            # Simulates the queue process when we pop values that should possibly answer the query
            while interval_queue and query >= interval_queue[0][0]:
                interval = interval_queue.popleft()
                heapq.heappush(heap, (interval[1] - interval[0] + 1, interval[1], interval[0]))

            # Simulates lazy removals from heap
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

            else:
                res[idx] = -1

        return res