class Solution:
    def fillInfinity(self,matrix,row,col):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0,c):
            if matrix[row][i] != 0:
                matrix[row][i] = float('inf')
        
        for j in range(0,r):
            if matrix[j][col] != 0:
                matrix[j][col] = float('inf')
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        # at first traversal convert the into inf
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    self.fillInfinity(matrix,i,j)
        
        # convert the filled inf into zero
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] =0
