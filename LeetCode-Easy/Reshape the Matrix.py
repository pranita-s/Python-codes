# TIME - O(RC)


def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        matrix=nums
        if len(matrix) * len(matrix[0]) != r * c:
            return nums
        
        reshape = [[0] * c for _ in range(r)]
        
        col = 0
        count= 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count += 1
                newRow = (count-1)//c
                if col >= c:
                    col = 0
                newCol = col
                reshaped[newRow][newCol] = matrix[i][j]
                col += 1
        return(reshaped)

