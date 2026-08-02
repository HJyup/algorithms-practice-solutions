import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        mp = {} # number of entries for each room
        # heap should have (end, index)
        meetings.sort(key = lambda x: (x[0], x[1]))

        rooms = [(0, i) for i in range(n)]
        heapq.heapify(rooms)

        for meeting in meetings:
            start, end = meeting[0], meeting[1]

            while start > rooms[0][0]:
                _, idx = heapq.heappop(rooms)
                heapq.heappush(rooms, (start, idx))

            time, idx = heapq.heappop(rooms)
            mp[idx] = mp.get(idx, 0) + 1

            duration = end - start
            heapq.heappush(rooms, (max(start, time) + duration, idx))

        ans = 0
        for i in mp:
            if mp[i] > mp[ans]:
                ans = i

        return ans