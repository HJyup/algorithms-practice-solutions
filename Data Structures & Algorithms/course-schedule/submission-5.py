from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We cannot take all schedules if and only if we have a cycle!
        seen = [0] * numCourses
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(i):
            if seen[i] == 1:
                return False

            if seen[i] == 2:
                return True

            seen[i] = 1
            for nei in graph[i]:
                if not dfs(nei):
                    return False

            seen[i] = 2
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False

        return True