class UnionFind:

    def __init__(self, nums: List[int]):
        self.parents = nums
        self.rank = [1] * len(nums)
    
    def find(self, node: int) -> int:
        found = node

        while found != self.parents[found]:
            # Path compression
            self.parents[found] = self.parents[self.parents[found]]
            found = self.parents[found]

        return found

    def union(self, u: int, v: int) -> int:
        parent_u, parent_v = self.find(u), self.find(v)

        if parent_u == parent_v:
            return False

        if self.rank[parent_u] > self.rank[parent_v]:
            self.parents[parent_v] = parent_u
            self.rank[parent_u] += 1

        else:
            self.parents[parent_u] = parent_v
            self.rank[parent_v] += 1

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nums = [i for i in range(n)]
        forest = UnionFind(nums)
        res = n

        for u, v in edges:
            if forest.union(u, v):
                res -= 1

        return res
