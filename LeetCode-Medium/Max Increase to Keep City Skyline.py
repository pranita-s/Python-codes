# TIME - O(RC)
# SPACE - O(R+C)

def maxIncreaseKeepingSkyline(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top_bottom = [-float('inf')] * len(grid[0])
        left_right = [-float('inf')] * len(grid)       
        for i in range(len(grid)):
            l_r = -float('inf')
            for j in range(len(grid[0])):
                top_bottom[j] = max(top_bottom[j],grid[i][j])
                l_r = max(l_r,grid[i][j])            
            left_right[i] = l_r
        
        diff = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff += min(top_bottom[j],left_right[i]) - grid[i][j]
        
        return diff
