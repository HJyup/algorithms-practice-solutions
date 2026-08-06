import collections

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # one parent (so only one node has outdegree of 1) -> 
        # Im idiot -> parent can be anything lol, if no cycle -> u can find at least one parent
        # no cycles -> DFS
        # number of connected components = 1 -> Seen
        seen = set()

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            seen.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue

                if nei in seen:
                    return False

                seen.add(nei)
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(seen) == n