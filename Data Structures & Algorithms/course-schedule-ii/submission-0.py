class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visited = set()
        path = set()
        res = []

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course) #no cycle on this course if all neighbors return True
            for n in adjList[course]:
                if not dfs(n):
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for n in range(numCourses):
            if n not in visited:
                if not dfs(n):
                    return []
        
        return res
