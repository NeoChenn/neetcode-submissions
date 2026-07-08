class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[b].append(a)

        prereqs = defaultdict(set)

        def dfs(course):
            if course in prereqs:
                return prereqs[course]
            
            for nei in adjList[course]:
                prereqs[course] |= dfs(nei)
                prereqs[course].add(nei)
            
            return prereqs[course]

        for i in range(numCourses):
            dfs(i)

        res = []
        for a, b in queries:
            res.append(a in prereqs[b])
        
        return res
        