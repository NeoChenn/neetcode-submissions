class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures) 
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
                continue
            while stack and temp > temperatures[stack[-1]]:
                cur = stack.pop()
                output[cur] = i - cur
            stack.append(i)
        return output