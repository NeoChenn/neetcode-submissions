class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            destroyed = False
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    destroyed = True
                    break
                else:
                    destroyed = True
                    break
            if not destroyed:
                stack.append(asteroid)
        return stack