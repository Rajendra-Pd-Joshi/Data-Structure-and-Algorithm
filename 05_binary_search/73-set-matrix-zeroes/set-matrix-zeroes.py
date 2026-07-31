class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # i 'm taking the first column and first row to keep track of zeros
        # step 1: if there is a zero in the first column make col0=1 and in first row make row0=1
        
        r = len(matrix)
        c = len(matrix[0])
        col0=0
        row0=0
        for i in range(0,r):
            if matrix[i][0]==0:
                col0 =1
        
        for j in range(0,c):
            if matrix[0][j]==0:
                row0=1
        
        # step 2: iterate over the matrix and if you found zero set matrix[i][0] =0 and matrix[0][j] = 0

        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
        # step 3: traverse form (1,1) and if matrix[i][0]==0 or matrix[0][j]==0 then put is 0
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        # step 4 : handel the first row and first column
        if col0==1:
            for i in range(0,r):
                matrix[i][0]=0
        
        if row0==1:
            for j in range(0,c):
                matrix[0][j]=0