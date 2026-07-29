import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [
            (-count, char)
            for count, char in [(a, "a"), (b, "b"), (c, "c")]
            if count != 0
        ]

        heapq.heapify(heap)
        ans = ""

        prev = None
        while heap:
            neg_count, val = heapq.heappop(heap)
            ans += val

            neg_count += 1
            if prev is not None:
                heapq.heappush(heap, prev)
                prev = None

            if neg_count != 0 and ((heap and -neg_count - (-heap[0][0]) >= 1) or not heap):
                neg_count += 1
                ans += val

            if neg_count != 0:
                prev = (neg_count, val)

        return ans