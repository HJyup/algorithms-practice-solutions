from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = [0] * n
        count = 0

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, p):
            nonlocal count 

            if seen[u] == 2:
                return True

            if seen[u] == 1:
                return False

            seen[u] = 1
            for v in g[u]:
                if v == p:
                    continue

                if not dfs(v, u):
                    return False

            seen[u] = 2
            count += 1

            return True
        
        dfs(0, None)        
        return count == n