class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parents = [ i for i in range(n) ]
        rank = [0] * n

        def find(u):
            curr = u

            while curr != parents[curr]:
                parents[curr] = parents[parents[curr]]
                curr = parents[curr]

            return curr

        def union(u, v):
            par_u, par_v = find(u), find(v)

            if par_u == par_v:
                return False

            if rank[par_u] > rank[par_v]:
                parents[par_v] = par_u
                rank[par_u] += 1

            else:
                parents[par_u] = par_v
                rank[par_v] += 1

            return True

        for u, v in edges:
            if not union(u - 1, v - 1):
                return [u, v]

        return []