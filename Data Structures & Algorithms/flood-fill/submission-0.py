class Solution:   
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel = image[sr][sc]
        #[1, 1, 1]
        #[1, 1, 0]
        #[1, 0, 1]
                  
        visited = set()
        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or (r, c) in visited or image[r][c] != pixel:
                return
                  
            visited.add((r, c))
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image