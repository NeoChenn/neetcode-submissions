class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #base case: if attempt == word, found = True 
        #if found == True, return
        #track index. If attempt != word at such index, return

        #choices: for each character, the adjacent characters
        maxRowIndex, maxColIndex = len(board) - 1, len(board[0]) - 1
        word = list(word)

        self.found = False
        attempt = []
        visited = []
        def backtrack(i, row, col):
            if attempt == word:
                self.found = True
                return
            if i >= len(word) or self.found or attempt[i] != word[i]:
                return

            #append letter and coords of accessible characters.
            choices = []
            if col + 1 <= maxColIndex and [row, col + 1] not in visited:
                choices.append([board[row][col + 1], row, col + 1])
            if row + 1 <= maxRowIndex and [row + 1, col] not in visited:
                choices.append([board[row + 1][col], row + 1, col])
            if col - 1 >= 0 and [row, col - 1] not in visited:
                choices.append([board[row][col - 1], row, col - 1])
            if row - 1 >= 0 and [row - 1, col] not in visited:
                choices.append([board[row - 1][col], row - 1, col])

            for char, r, c in choices:
                attempt.append(char)
                visited.append([r, c])
                backtrack(i + 1, r, c)
                attempt.pop()
                visited.pop()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if not self.found:
                    attempt.append(board[r][c])
                    visited.append([r, c])
                    backtrack(0, r, c)
                    attempt.pop()
                    visited.pop()

        return self.found

