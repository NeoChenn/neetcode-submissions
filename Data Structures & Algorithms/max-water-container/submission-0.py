class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                area = max(area, (min(heights[i], heights[j]) * (j - i)))
        
        return area
