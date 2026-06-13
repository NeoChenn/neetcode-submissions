class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #one lane road

        #sort the positions [(0, 1), (1, 2), (4, 2), (7, 1)].
        #Starting from car closest to target, calculate time to reach target.
        #if time <= top of stack, ignore it.
        #if time > top of stack. append it.
        
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack.append(pair[0])
        for i in range(1, len(pair)):
            time = (target-pair[i][0]) / pair[i][1]
            stackTime = (target-stack[-1][0]) / stack[-1][1]
            if time > stackTime:
                stack.append(pair[i])
        
        return len(stack)