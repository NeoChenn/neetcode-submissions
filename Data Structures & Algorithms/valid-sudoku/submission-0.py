class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            map = {}
            for j in range(9):
                if board[i][j] in map:
                    return False
                if board[i][j] == '.':
                    continue
                if board[i][j] not in map:
                    map[board[i][j]] = 1
                    continue
        
        for j in range(9):
            map = {}
            for i in range(9):
                if board[i][j] in map:
                    return False
                if board[i][j] == '.':
                    continue
                if board[i][j] not in map:
                    map[board[i][j]] = 1
                    continue

        for i in range(3):
            for j in range(3):
                map = {}
                for a in range(3):
                    for b in range(3):
                        if board[3*i + a][3*j + b] in map:
                            return False
                        if board[3*i + a][3*j + b] == '.':
                            continue
                        if board[3*i + a][3*j + b] not in map:
                            map[board[3*i + a][3*j + b]] = 1
                            continue

                #3i, 3i + 1, 3i + 2
                #3j, 3j + 1, 3j + 2

        return True