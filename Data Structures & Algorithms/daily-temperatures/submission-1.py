class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #temps = [30, 38, 30, 36, 35, 40, 28]
        #res = [1, 4, 1, 2, 1, 0, 0]
        #monoDecreasingStack = [5, 6]

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[i] > temperatures[stack[-1]]:
                a = stack.pop()
                res[a] = i - a
            stack.append(i)

        return res  