class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = collections.deque()
        for course, dependencies in enumerate(indegree):
            if dependencies == 0:
                queue.append(course)

        idx = 0
        schedule = []

        while queue:
            course = queue.popleft()
            idx += 1

            schedule.append(course)
            for nei_course in graph[course]:
                indegree[nei_course] -= 1
                if indegree[nei_course] == 0:
                    queue.append(nei_course)

        if idx != numCourses:
            return []

        return schedule