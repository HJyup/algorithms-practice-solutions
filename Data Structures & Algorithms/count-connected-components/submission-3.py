class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        res = n

        def find(node: int) -> int:
            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res

        def union(u: int, v: int) -> bool: 
            parent_u, parent_v = find(u), find(v)

            if parent_u == parent_v:
                return False

            if rank[parent_v] > rank[parent_u]:
                parent[parent_u] = parent_v
                rank[parent_v] += 1
            else:
                parent[parent_v] = parent_u
                rank[parent_u] += 1

            return True

        for u, v in edges:
            if union(u, v):
                res -= 1

        return res
