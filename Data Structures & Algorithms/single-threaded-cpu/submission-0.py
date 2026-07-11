class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #Sort tasks by enqueue time (keeping original indices)
        #Maintain a min heap of (processingTime, index) for tasks that are currently available
        #Track curTime

        #At each step:
        #Push all tasks with enqueueTime <= curTime into the heap
        #If heap is empty (CPU idle), jump curTime to the next task's enqueue time and push it
        #Pop the task with shortest processing time from heap, add its index to result, advance curTime by its processing time
        #Repeat until all tasks processed

        #[[2, 1], [3, 3], [4, 1], [4, 4], [5, 2]]
        
        h = []
        res = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        curTime = tasks[0][0]
        i = 0
        while i < len(tasks) or h:
            while i < len(tasks) and tasks[i][0] <= curTime:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            if not h:
                curTime = tasks[i][0]
                continue
            t = heapq.heappop(h)
            curTime += t[0]
            res.append(t[1])
        return res