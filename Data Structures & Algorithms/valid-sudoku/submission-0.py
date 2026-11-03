class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)
        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                if (curr == "."):
                    continue
                    
                if (curr in rows[row]):
                    return False
                if (curr in cols[col]):
                    return False
                if (curr in square[row // 3 , col // 3]):
                    return False

                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                square[(row // 3, col // 3)].add(board[row][col])
        return True