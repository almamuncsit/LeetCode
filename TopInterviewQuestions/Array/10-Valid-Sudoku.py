from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                # Check row
                if not self.checkRow(board, i, j):
                    return False
                
                # Check Column
                if not self.checkColumn(board, i, j):
                    return False

                # Check sub-boxes
                if not self.checkSubBox(board, i, j):
                    return False

        return True


    def checkRow(self, board, i, j):
        for x in range(9):
            if x != j and board[i][x] != '.' and board[i][x] == board[i][j]:
                return False
        return True


    def checkColumn(self, board, i, j):
        for x in range(9):
            if x != j and board[x][i] != '.' and board[x][i] == board[j][i]:
                return False
        return True


    def checkSubBox(self, board, i, j):
        new_i = self.starPointer(i)
        new_j = self.starPointer(j)
        for x in range(new_i, new_i+3):
            for y in range(new_j, new_j+3):
                if x == i and y == j:
                    continue
                if board[x][y] != '.' and board[x][y] == board[i][j]:
                    return False
        return True


    def starPointer(self, index):
        if index in [0, 1, 2]:
            return 0
        elif index in [3, 4, 5]:
            return 3
        else:
            return 6



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
