from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        LOCK_LENGTH = 4

        def to_number(lock: str) -> Tuple[int]:
            return tuple(int(digit) for digit in lock)

        locked = { to_number(deadend) for deadend in deadends }
        start = (0, 0, 0, 0)
        q = deque([(start, 0)])
        target = to_number(target)

        if start in locked:
            return -1

        while q:
            n = len(q)

            for _ in range(n):
                lock, cost = q.popleft()
                if lock == target:
                    return cost

                locked.add(lock)
                for digit in range(LOCK_LENGTH):
                    nei = list(lock)

                    nei[digit] = (nei[digit] + 1) % 10
                    nei = tuple(nei)

                    if nei not in locked:
                        locked.add(nei)
                        q.append((nei, cost + 1))

                    nei = list(lock)

                    nei[digit] = (nei[digit] - 1) % 10
                    nei = tuple(nei)

                    if nei not in locked:
                        locked.add(nei)
                        q.append((nei, cost + 1))

        return -1