from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Have one root only. 
        # Cannot have not connected components
        # Cannot have cycles (in undicrted graph we should store parent as a variable)
        graph = defaultdict(list)
        seen = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i, parent):
            if seen[i]:
                return False

            seen[i] = True
            for nei in graph[i]:
                if nei == parent:
                    continue

                if not dfs(nei, i):
                    return False

            return True
            
        # Cycle check
        if not dfs(0, None):
            return False

        # Connectivity check
        for visited in seen:
            if not visited:
                return False

        return True


        