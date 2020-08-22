from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row
        if not self.checkRow(board):
            return False
        
        # Check Column
        if not self.checkColumn(board):
            return False

        # Check sub-boxes
        if not self.checkSubBox(board):
            return False

        return True


    def checkRow(self, board):
        for i in range(9):
            row = [i for i in board[i] if i != '.']
            if len(row) != len(set(row)):
                return False    
        return True


    def checkColumn(self, board):
        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != '.':
                    col.append(board[j][i])
            if len(col) != len(set(col)):
                return False
        return True


    def checkSubBox(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                box = [i for i in box if i != '.']
                if len(box) != len(set(box)):
                    return False
        return True



sol = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
valid = sol.isValidSudoku(board)
print(valid)
