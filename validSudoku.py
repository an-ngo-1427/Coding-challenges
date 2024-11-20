    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowDict = {}
        colDict = {}
        subBoxDict = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if j not in colDict:
                    colDict[j] = []
                    colDict[j].append(board[i][j])
                else:
                    if(board[i][j] in colDict[j]  and board[i][j] != '.'):
                        return False
                    else:
                        colDict[j].append(board[i][j])

                if i not in rowDict:
                    rowDict[i] = [board[i][j]]
                else:
                    if(board[i][j] in rowDict[i] and board[i][j] != '.'):
                        print(board[i][j])
                        print('enterewd',rowDict)
                        return False
                    else:
                        rowDict[i].append(board[i][j])

                boxCoor = [i//3,j//3]
                if(boxCoor not in subBoxDict):
                    subBoxDict[boxCoor]
