class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []

        enqueueTime = [ (task[0], i) for i, task in enumerate(tasks) ]
        heapq.heapify(enqueueTime)

        processingTime = []
        processed = 0

        time = 0
        while processed < len(tasks):
            if enqueueTime and enqueueTime[0][0] > time:
                time = enqueueTime[0][0] 

            while enqueueTime and enqueueTime[0][0] <= time:
                _, idx = heapq.heappop(enqueueTime)
                heapq.heappush(processingTime, (tasks[idx][1], idx))
            
            if processingTime:
                process_to_complete, idx = heapq.heappop(processingTime)
                res.append(idx)

                time += process_to_complete
                processed += 1

        return res