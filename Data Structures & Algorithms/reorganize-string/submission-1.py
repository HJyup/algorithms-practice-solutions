from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = defaultdict(int)
        ans = []

        for ch in s:
            mp[ch] += 1

        heap = [(-count, ch) for ch, count in mp.items()]
        heapq.heapify(heap)

        prev = None
        while heap:
            neg_count, ch  = heapq.heappop(heap)
            ans.append(ch)

            if prev is not None:
                heapq.heappush(heap, prev)
                prev = None

            new_count = neg_count + 1
            if new_count != 0:
                prev = (new_count, ch)

        return ''.join(ans) if prev is None else ""