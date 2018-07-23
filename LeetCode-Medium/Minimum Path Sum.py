# TIME - O(RC)
# SPACE - O(RC)

def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        #row1
        dp[0][0] = grid[0][0]
        for i in range(1,len(grid[0])):
            dp[0][i] = dp[0][i-1]  + grid[0][i]
        for i in range(1,len(grid)):
            dp[i][0] = dp[i-1][0]  + grid[i][0]
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
  
# TIME - O(RC)
# SPACE - O(C)
  
 def minPathSum(grid):
  dp = list(grid[0])
  for i in range(1,len(grid[0])):
    dp[i] += dp[i-1]
  
  for i in range(1,len(grid)):
    dp[0] += grid[i][0]
    for j in range(1,len(grid[0])):
      dp[j] = min(dp[j-1],dp[j]) + grid[i][j]
  return dp[-1]
