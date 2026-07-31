class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #BFS attempting each possible state and keeping track of levels
        #keep track of a visited set

        visited = set()
        for deadend in deadends:
            visited.add(deadend)
        
        if "0000" in visited:
            return -1
        visited.add("0000")

        q = deque(["0000"])
        level = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(4):
                    nei1 = list(cur)
                    nei2 = list(cur)
                    if nei1[i] == '9':
                        nei1[i] = '0'
                    else: 
                        nei1[i] = str(int(nei1[i]) + 1)
                    if nei2[i] == '0':
                        nei2[i] = '9'
                    else:
                        nei2[i] = str(int(nei2[i]) - 1)
                    if "".join(nei1) == target or "".join(nei2) == target:
                        return level
                    if "".join(nei1) not in visited:
                        visited.add("".join(nei1))
                        q.append("".join(nei1))
                    if "".join(nei2) not in visited:
                        visited.add("".join(nei2))
                        q.append("".join(nei2))
                #append all possible turns to queue
                #if any combination is a target, return level
                #skip if combination in visited
            level += 1
        return -1