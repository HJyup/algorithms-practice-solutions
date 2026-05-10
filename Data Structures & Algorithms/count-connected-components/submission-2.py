from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        res = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i):
            if i in visited:
                return 

            visited.add(i)
            for neighbour in graph[i]:
                dfs(neighbour)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res        