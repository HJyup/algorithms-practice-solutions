class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)

        visit = [0] * numCourses
        order = []

        def dfs(u):
            if visit[u] == 1:
                return False

            if visit[u] == 2:
                return True

            visit[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False

            visit[u] = 2
            order.append(u)

            return True

        for u in range(numCourses):
            if not dfs(u):
                return []

        return order
                
        