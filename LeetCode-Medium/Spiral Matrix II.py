# TIME - O(n**2)

def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0 for _ in range(n)] for _ in range(n)]
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        num = 1
        x = y = d = 0
        for _ in range(n**2):
            mat[x][y] = num
            num += 1
            next_x,next_y = x + direction[d][0],y + direction[d][1]
            if (next_x not in range(n) or next_y not in range(n) or mat[next_x][next_y] !=0):
                d = (d+1)%4
                next_x,next_y = x + direction[d][0], y + direction[d][1]
            x,y = next_x,next_y
        
        return mat
            
