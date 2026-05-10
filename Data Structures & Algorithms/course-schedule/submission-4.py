class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses
        def dfs(idx):
            if state[idx] == 1:
                return False

            if state[idx] == 2:
                return True
            
            state[idx] = 1
            for course in graph[idx]:
                if not dfs(course):
                    return False

            state[idx] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0 and not dfs(course):
                return False

        return True

        
        