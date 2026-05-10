from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited, visiting = set(), set()

        for required_course, course in prerequisites:
            graph[course].append(required_course)

        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False

            visiting.add(course)

            for prereq in graph.get(course, []):
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
                
        return True

        

        