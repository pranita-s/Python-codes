# TIME - O(n!)
# SPACE - O(n)


def totalNQueens(n):
        """
        :type n: int
        :rtype: int
        """
        
        def placeQueen(row):
            if row == n:
                result[0]+=1
                return
            for c in range(n):
                if all(abs(col-c) not in (0,row-rowNum) for rowNum,col in enumerate(placement[:row])):
                    placement[row] = c
                    placeQueen(row+1)
                    
        result = [0]
        placement = [0]*n
        placeQueen(0)
        return result[0]
        
