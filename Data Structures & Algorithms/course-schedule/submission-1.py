class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        self.loop = False
        for i in range(numCourses):
            adjList[i] = []
        for course, prereq in prerequisites:
            adjList[course].append(prereq) 

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            visited.add(course)
            return True

        #check for loops using the visited set
        #if every course has been visited and there has been no loops, return true

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        