class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #indices represent position
        #positive means right, negative means left
        #absolute value represents size

        #for each asteroid, compare with top of stack. 
        #if same sign or stack empty, append it. 
        #If different sign,
        #if larger than top stack, pop from stack and append it
        #if smaller, do nothing
        #If equal, pop from stack.
        stack = []

        for asteroid in asteroids:
            while True:
                if len(stack) == 0 or not (stack[-1] > 0 and asteroid < 0):
                    stack.append(asteroid)
                    break
                else:
                    if abs(asteroid) > abs(stack[-1]):
                        stack.pop()
                        continue
                    elif abs(asteroid) == abs(stack[-1]):
                        stack.pop()
                        break
                    else:
                        break

        return stack