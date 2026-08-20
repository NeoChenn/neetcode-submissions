class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for course in range(numCourses):
            adjList[course] = []
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        visited = set()
        path = set()

        def checkCycle(course):
            if course in visited:
                return False
            if course in path:
                return True
            
            path.add(course)
            for adjCourse in adjList[course]:
                 if checkCycle(adjCourse):
                    return True
            path.remove(course)
            visited.add(course)
            return False

        for course in range(numCourses):
            if checkCycle(course):
                return False
        return True