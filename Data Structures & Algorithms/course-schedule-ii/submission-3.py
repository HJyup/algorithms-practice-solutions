from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 -> 1: [0, 1] (0 depends on 1)
        graph = defaultdict(list)
        seen = [0] * numCourses
        res = []

        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(node):
            nonlocal path

            if seen[node] == 1:
                return False

            if seen[node] == 2:
                return True

            seen[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            seen[node] = 2
            path.append(node)

            return True

        for node in range(numCourses):
            path = []
            if not dfs(node):
                return []
            res += path 

        return res