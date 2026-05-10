class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [ num for num in range(len(edges)) ]
        rank = [ num for num in range(len(edges)) ]

        def find(u: int) -> int:
            current = u

            while current != parents[current]:
                parents[current] = parents[parents[current]]
                current = parents[current]

            return current

        def union(u: int, v: int) -> bool:
            u_parent, v_parent = find(u), find(v)

            if u_parent == v_parent:
                return False

            if rank[u_parent] > rank[v_parent]:
                parents[v_parent] = u_parent

            elif rank[u_parent] < rank[v_parent]:
                parents[u_parent] = v_parent

            else:
                parents[v_parent] = u_parent
                rank[u_parent] += 1

            return True

        for u, v in edges:
            if not union(u - 1, v - 1):
                return [u, v]

        return []
        