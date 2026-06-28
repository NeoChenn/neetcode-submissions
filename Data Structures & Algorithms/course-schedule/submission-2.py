class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for a, b in prerequisites:
            adjList[a].append(b)

        visited = set()
        path = set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            path.remove(course)
            visited.add(course)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True