from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mp = defaultdict(set) # node : which other nodes it unlocks

        graph = defaultdict(list)
        out = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            out[v] += 1

        q = deque([node for node in range(numCourses) if out[node] == 0])
        while q:
            node = q.popleft()

            for nei in graph[node]:
                mp[nei].update(mp[node])
                mp[nei].add(node)

                out[nei] -= 1
                if out[nei] == 0:
                    q.append(nei)

        ans = []
        for u, v in queries:
            ans.append(u in mp[v])

        return ans
