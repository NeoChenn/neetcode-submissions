class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        BFS
        create a set, where we add the deadends, and the value of wheels already visited
        do not add to deque if in set
        """
        
        invalid = set()
        for deadend in deadends:
            invalid.add(deadend)
        if "0000" in invalid:
            return -1

        invalid.add("0000")
        level = 0
        q = deque([[0, 0, 0, 0]])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if "".join(str(x) for x in curr) == target:
                    return level
                for i in range(4):
                    #neighbor generation. add to invalid set, and to queue
                    fst, snd = curr.copy(), curr.copy()
                    if curr[i] == 9:
                        fst[i] = 0
                    else:
                        fst[i] += 1
                    if curr[i] == 0:
                        snd[i] = 9
                    else:
                        snd[i] -= 1
                    if "".join(str(x) for x in fst) not in invalid:
                        q.append(list(fst))
                        invalid.add("".join(str(x) for x in fst))
                    if "".join(str(x) for x in snd) not in invalid:
                        q.append(list(snd))
                        invalid.add("".join(str(x) for x in snd))
            level += 1

        return -1