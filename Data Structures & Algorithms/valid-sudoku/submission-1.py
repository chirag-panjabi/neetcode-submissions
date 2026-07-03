class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this solution is what i did on my first try without reference
        for i in range(9): # vertical and horizontal lines test
            seen_x = set()
            seen_y = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen_x:
                        return False
                    else:
                        seen_x.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in seen_y:
                        return False
                    else:
                        seen_y.add(board[j][i])

        square_indexes = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        # to test squares
        for i in range(3):
            i = 3*i # 0,3,6
            for j in range(3):
                seen = set()
                j = 3*j
                for index in square_indexes:
                    val = board[index[0]+i][index[1]+j]
                    if val == '.':
                        continue
                    else:
                        if val in seen:
                            return False
                        else:
                            seen.add(val)



        return True
                
            
            