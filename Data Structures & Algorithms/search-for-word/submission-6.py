class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if dfs(nr, nc, i + 1):
                    return True
            visited.remove((r, c))
            return False
            
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
