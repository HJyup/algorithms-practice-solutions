from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # u cannot finish a course if it's a cycle of courses :)
        graph = defaultdict(list)

        for u, v in prerequisites:
            # to take course b we need to take course a
            graph[u].append(v)

        seen = [0] * numCourses # 0 - not visied, 1 - current cycle, 2 - fully finished
        # why we need 3 things.
        # 1. in directed graph some sabparts of the component can be visited several times
        # depending on where we do a start node

        def dfs(node: int) -> bool:
            if seen[node] == 1:
                return False

            if seen[node] == 2:
                return True

            seen[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            seen[node] = 2
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False

        return True